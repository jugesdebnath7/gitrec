# src/gitrec/domain/mapper/repository/tag_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.tag_item import TagItem


class TagMapper:
    """
    Maps GitHub tag responses into domain tag entities.
    """

    @staticmethod
    def to_tag_item(
        data: dict[str, Any],
        repo_id: int,
        created_at: str,
    ) -> TagItem:
        """
        Convert a GitHub tag response into a TagItem.

        Args:
            data: Raw tag data returned by the GitHub API.
            repo_id: Unique identifier of the repository containing the tag.
            created_at: Timestamp associated with the tag, obtained from
                additional Git metadata when available.

        Returns:
            A TagItem representing the repository tag.
        """
        return TagItem(
            repo_id=repo_id,
            tag_name=data["name"],
            commit_sha=data["commit"]["sha"],
            created_at=created_at,
        )
