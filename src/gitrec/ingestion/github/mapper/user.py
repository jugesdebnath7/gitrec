# src/gitrec/ingestion/github/mapper/users.py

from __future__ import annotations

from src.gitrec.ingestion.github.client import JSON
from src.gitrec.ingestion.github.schemas.user import UserSearchResult


class UserSearchMapper:
    @staticmethod
    def to_search_results(
        user_data: JSON,
    ) -> list[UserSearchResult]:
        """
        Map raw user data to a list of UserSearchResult objects.

        Args:
            user_data (dict): Raw user data from the GitHub API.

        Returns:
            list[UserSearchResult]: A list of mapped UserSearchResult objects.
        """
        return [
            UserSearchResult(
                login=user["login"],
            )
            for user in user_data.get("items", [])
            if "login" in user
        ]