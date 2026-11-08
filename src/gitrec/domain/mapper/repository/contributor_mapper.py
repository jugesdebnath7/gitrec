# src/gitrec/domain/mapper/repository/contributor_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.contributor_item import ContributorItem


class ContributorMapper:
    """
    Maps GitHub contributor responses into domain contributor entities.
    """

    @staticmethod
    def to_contributor_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> ContributorItem:
        """
        Convert a GitHub contributor response into a ContributorItem.

        Args:
            data: Raw contributor data returned by the GitHub API.
            repo_id: Unique identifier of the repository to which the
                contributor has contributed.

        Returns:
            A ContributorItem representing the repository contributor.
        """
        return ContributorItem(
            repo_id=repo_id,
            user_id=data["id"],
            login=data["login"],
            contributions=data["contributions"],
            type=data["type"],
        )
