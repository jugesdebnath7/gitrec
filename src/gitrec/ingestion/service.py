# src/gitrec/ingestion/service.py

from __future__ import annotations

import logging
from dataclasses import dataclass

from src.gitrec.domain.entity.repository.repository_item import RepositoryItem
from src.gitrec.domain.entity.user.user_item import UserItem

from src.gitrec.domain.mapper.repository.repository_mapper import RepositoryMapper
from src.gitrec.domain.mapper.user.user_mapper import UserMapper

from src.gitrec.ingestion.github.endpoints import (
    repository as repository_endpoint,
    user as user_endpoint,
)
from src.gitrec.ingestion.github.loader import GitHubLoader
from src.gitrec.ingestion.github.mapper.repository import RepositorySearchMapper
from src.gitrec.ingestion.github.mapper.user import UserSearchMapper
from src.gitrec.ingestion.github.search import GitHubSearch, QueryParams


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class IngestionResult:
    """Result produced by the ingestion service."""

    repositories: list[RepositoryItem]
    users: list[UserItem]


class IngestionService:
    """
    Orchestrates GitHub search, resource loading, and domain mapping.

    The service coordinates the ingestion workflow but delegates resource
    mapping to the aggregate-level RepositoryMapper and UserMapper.
    """

    def __init__(
        self,
        github_search: GitHubSearch,
        github_loader: GitHubLoader,
        *,
        test_limit: int | None = None,
    ) -> None:
        self._github_search = github_search
        self._github_loader = github_loader
        self._test_limit = test_limit

    def run(self) -> IngestionResult:
        """
        Execute the GitHub ingestion workflow.

        Returns:
            An IngestionResult containing mapped repository and user entities.
        """
        logger.info("Starting ingestion service.")

        repository_results, user_results = self._search_github()

        repository_results = self._apply_limit(repository_results)
        user_results = self._apply_limit(user_results)

        logger.info(
            "Loading resources: repositories=%d users=%d",
            len(repository_results),
            len(user_results),
        )

        repository_resources = self._load_repositories(
            repository_results
        )
        user_resources = self._load_users(
            user_results
        )

        repositories = [
            RepositoryMapper.to_repository_item(resource)
            for resource in repository_resources
        ]

        users = [
            UserMapper.to_user_item(resource)
            for resource in user_resources
        ]

        logger.info(
            "Ingestion service completed: repositories=%d users=%d",
            len(repositories),
            len(users),
        )

        return IngestionResult(
            repositories=repositories,
            users=users,
        )

    def _search_github(self):
        """Search GitHub for repositories and users."""

        repository_query: QueryParams = {
            "q": "language:python stars:>1000",
        }

        user_query: QueryParams = {
            "q": "location:San Francisco",
        }

        repository_search = self._github_search.repositories(
            repository_query
        )

        user_search = self._github_search.users(
            user_query
        )

        repository_results = RepositorySearchMapper.to_search_results(
            repo_data=repository_search,
        )

        user_results = UserSearchMapper.to_search_results(
            user_data=user_search,
        )

        return repository_results, user_results

    def _load_repositories(self, repositories):
        """Load complete resources for the selected repositories."""

        logger.info(
                "Preparing repository resources: count=%d",
                len(repositories),
        )

        endpoints = [
            repository_endpoint(
                repository.owner,
                repository.name,
            )
            for repository in repositories
        ]

        resources = self._github_loader.load_repositories(
            repositories=endpoints,
        )

        logger.info(
            "Repository resources loaded: count=%d",
            len(resources),
        )

        return resources

    def _load_users(self, users):
        """Load complete resources for the selected users."""

        logger.info(
                "Preparing user resources: count=%d",
                len(users),
        )

        endpoints = [
            user_endpoint(user.login)
            for user in users
        ]

        resources = self._github_loader.load_users(
            users=endpoints,
        )

        logger.info(
            "User resources loaded: count=%d",
            len(resources),
        )

        return resources

    def _apply_limit(self, items):
        """Apply the optional ingestion limit used for development/testing."""

        if self._test_limit is None:
            return items

        return items[:self._test_limit]
