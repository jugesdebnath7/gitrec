# src/gitrec/ingestion/service.py

from __future__ import annotations

import logging

from src.gitrec.ingestion.github.endpoints import (
    repository as repository_endpoint, 
    user as user_endpoint,
)
from src.gitrec.ingestion.github.loader import GitHubLoader  
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
        logger.info("Starting ingestion service...")

        # Example search query parameters
        repo_query_params: QueryParams = {"q":"language:python stars:>1000"}
        user_query_params: QueryParams = {"q":"location:San Francisco"}

        # Search for repositories and users
        repo_results = self._github_search.repositories(repo_query_params)
        user_results = self._github_search.users(user_query_params)

        # Load repository and user resources
        self._github_loader.load_repositories(repositories=repo_results)
        self._github_loader.load_users(users=user_results)

        logger.info("Ingestion service completed.")