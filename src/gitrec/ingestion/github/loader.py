# src/gitrec/ingestion/github/loader.py

"""
GitHub resource loading.

Provides components for loading repository and user resources from the
GitHub API. Resource loaders coordinate endpoint retrieval while
delegating HTTP communication to the GitHub client.
"""

from __future__ import annotations

import logging
from typing import Any

from gitrec.core.exceptions import (
    APITimeoutError,
    GitHubAPIError,
    NetworkError,
    NotFoundError,
    RateLimitError,
)
from gitrec.ingestion.github.client import GitHubClient, JSON

from .endpoints import RepositoryEndpoints, UserEndpoints


logger = logging.getLogger(__name__)


LoaderResult = dict[str, Any]
"""Loaded GitHub resource collection."""


class ResourceLoader:
    """
    Shared GitHub resource loader.

    Executes GitHub API requests safely and aggregates responses from
    multiple endpoints.
    """

    def __init__(self, client: GitHubClient) -> None:
        """
        Initialize the resource loader.

        Args:
            client:
                Configured GitHub API client.
        """
        self._client = client

    def _safe_get(self, endpoint: str) -> JSON:
        """
        Execute a GitHub API request.

        Args:
            endpoint:
                GitHub API endpoint.

        Returns:
            Parsed API response or an error payload.
        """
        try:
            return self._client.get(endpoint)

        except (
            APITimeoutError,
            GitHubAPIError,
            NetworkError,
            NotFoundError,
            RateLimitError,
        ) as exc:
            logger.warning(
                "GitHub endpoint failed. endpoint=%s error=%s",
                endpoint,
                exc,
            )

            return {
                "success": False,
                "error": str(exc),
                "endpoint": endpoint,
            }

    def load_resources(
        self,
        endpoints: dict[str, str | None],
    ) -> LoaderResult:
        """
        Load multiple GitHub resources.

        Args:
            endpoints:
                Mapping of resource names to GitHub API endpoints.

        Returns:
            Loaded resources keyed by resource name.
        """
        return {
            name: self._safe_get(endpoint)
            for name, endpoint in endpoints.items()
            if endpoint is not None
        }


class RepositoryLoader:
    """
    Loads repository-related GitHub resources.
    """

    def __init__(
        self,
        resource_loader: ResourceLoader,
    ) -> None:
        """
        Initialize the repository loader.

        Args:
            resource_loader:
                Shared resource loader.
        """
        self._resource_loader = resource_loader

    def load(
        self,
        repository: RepositoryEndpoints,
    ) -> LoaderResult:
        """
        Load repository resources.

        Args:
            repository:
                Repository endpoint collection.

        Returns:
            Loaded repository resources.
        """
        return self._resource_loader.load_resources(
            {
                "repository": repository.base,
                "topics": repository.topics,
                "languages": repository.languages,
                "contributors": repository.contributors,
                "commits": repository.commits,
                "releases": repository.releases,
                "branches": repository.branches,
                "tags": repository.tags,
                "issues": repository.issues,
                "pulls": repository.pulls,
                "forks": repository.forks,
                "stargazers": repository.stargazers,
                "subscribers": repository.subscribers,
                "readme": repository.readme,
                "commit": repository.commit,
                "branch": repository.branch,
                "release": repository.release,
                "issue": repository.issue,
                "pull_request": repository.pull_request,
                "contents": repository.contents,
            }
        )


class UserLoader:
    """
    Loads user-related GitHub resources.
    """

    def __init__(
        self,
        resource_loader: ResourceLoader,
    ) -> None:
        """
        Initialize the user loader.

        Args:
            resource_loader:
                Shared resource loader.
        """
        self._resource_loader = resource_loader

    def load(
        self,
        user: UserEndpoints,
    ) -> LoaderResult:
        """
        Load user resources.

        Args:
            user:
                User endpoint collection.

        Returns:
            Loaded user resources.
        """
        return self._resource_loader.load_resources(
            {
                "user": user.base,
                "profile": user.profile,
                "repositories": user.repositories,
                "starred": user.starred,
                "followers": user.followers,
                "following": user.following,
                "organizations": user.organizations,
                "gists": user.gists,
                "events": user.events,
                "received_events": user.received_events,
            }
        )


class GitHubLoader:
    """
    Facade for loading GitHub resources.
    """

    def __init__(
        self,
        repo_loader: RepositoryLoader,
        user_loader: UserLoader,
    ) -> None:
        """
        Initialize the GitHub loader.

        Args:
            repo_loader:
                Repository resource loader.

            user_loader:
                User resource loader.
        """
        self._repo_loader = repo_loader
        self._user_loader = user_loader

    def load_repositories(
        self,
        repositories: list[RepositoryEndpoints],
    ) -> list[LoaderResult]:
        """
        Load resources for multiple repositories.

        Args:
            repositories:
                Repository endpoint collections.

        Returns:
            Loaded repository resource collections.
        """
        return [
            self._repo_loader.load(repository)
            for repository in repositories
        ]

    def load_users(
        self,
        users: list[UserEndpoints],
    ) -> list[LoaderResult]:
        """
        Load resources for multiple users.

        Args:
            users:
                User endpoint collections.

        Returns:
            Loaded user resource collections.
        """
        return [
            self._user_loader.load(user)
            for user in users
        ]