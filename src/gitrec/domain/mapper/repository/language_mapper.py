# src/gitrec/domain/mapper/repository/language_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.language_item import LanguageItem


class LanguageMapper:
    """
    Maps GitHub repository language responses into domain language entities.
    """

    @staticmethod
    def to_language_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> list[LanguageItem]:
        """
        Convert a GitHub languages response into LanguageItem entities.

        Args:
            data: Raw language data returned by the GitHub API.
            repo_id: Unique identifier of the repository using the languages.

        Returns:
            A list of LanguageItem instances representing the programming
            languages used by the repository.
        """
        return [
            LanguageItem(
                repo_id=repo_id,
                language=language,
            )
            for language in data
        ]
