# src/gitrec/ingestion/github/mapper/repositories.py

from __future__ import annotations

from src.gitrec.ingestion.github.client import JSON
from src.gitrec.ingestion.github.schemas.repository import RepositorySearchResult


class RepositorySearchMapper:
    @staticmethod
    def to_search_results(
        repo_data: JSON,
    ) -> list[RepositorySearchResult]:
        """
        Map raw repository data to a list of RepositorySearchResult objects.

        Args:
            repo_data (dict): Raw repository data from the GitHub API.

        Returns:
            list[RepositorySearchResult]: A list of mapped RepositorySearchResult objects.
        """
        return [
            RepositorySearchResult(
                owner=repo["owner"]["login"], 
                name=repo["name"],
            )
            for repo in repo_data.get("items", [])
            if repo.get("owner", {}).get("login")
            and repo.get("name")
        ]
