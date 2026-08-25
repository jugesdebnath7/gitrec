# src/gitrec/ingestion/service.py

from __future__ import annotations

import logging

from src.gitrec.ingestion.github.endpoints import (
    repository as _repository_endpoint, 
    user as _user_endpoint,
)
from src.gitrec.ingestion.github.loader import GitHubLoader  
from src.gitrec.ingestion.github.mapper.repository import RepositorySearchMapper
from src.gitrec.ingestion.github.mapper.user import UserSearchMapper
from src.gitrec.ingestion.github.search import GitHubSearch, QueryParams


logger = logging.getLogger(__name__)


class IngestionService:
    def __init__(
            self,
            github_search: GitHubSearch,
            github_loader: GitHubLoader,
    ) -> None:
        self._github_search = github_search
        self._github_loader = github_loader

    def run(self) -> None:
        """
        Execute the ingestion service.

        This method orchestrates the GitHub search and loading process.
        It retrieves repository and user data based on search queries
        and loads the corresponding resources.
        """
        # Temporary testing limits
        test_limit = 1

        logger.info("Starting ingestion service...")

        # Example search query parameters
        repo_query_params: QueryParams = {"q":"language:python stars:>1000"}
        user_query_params: QueryParams = {"q":"location:San Francisco"}

        # Search for repositories and users
        repo_search = self._github_search.repositories(repo_query_params)
        user_search = self._github_search.users(user_query_params)

        # Mapping for repositories and users
        repo_data_mapped = RepositorySearchMapper.to_search_results(repo_data=repo_search)
        user_data_mapped = UserSearchMapper.to_search_results(user_data=user_search)

        repo_data_mapped = repo_data_mapped[:test_limit]
        user_data_mapped = user_data_mapped[:test_limit]

        logger.info(
            "Loading resources: repositories=%d users=%d",
            len(repo_data_mapped),
            len(user_data_mapped),
        )

        # Endpoints for repositories and users
        repo_endpoint = [
            _repository_endpoint(
                repo.owner,
                repo.name,
            )
            for repo in repo_data_mapped
        ]
        
        user_endpoint = [
            _user_endpoint(
                user.login,
            )
            for user in user_data_mapped
        ]

        # Load repository and user resources
        repo_data = self._github_loader.load_repositories(repositories=repo_endpoint)
        user_data = self._github_loader.load_users(users=user_endpoint)

        print("Loaded repository data:", repo_data)
        print("Loaded user data:", user_data)

        logger.info("Ingestion service completed.")
        