# src/gitrec/domain/mapper/repository/release_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.release_item import ReleaseItem


class ReleaseMapper:
    """
    Maps GitHub release responses into domain release entities.
    """

    @staticmethod
    def to_release_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> ReleaseItem:
        """
        Convert a GitHub release response into a ReleaseItem.

        Args:
            data: Raw release data returned by the GitHub API.
            repo_id: Unique identifier of the repository to which the
                release belongs.

        Returns:
            A ReleaseItem representing the repository release.
        """
        author = data.get("author") or {}

        return ReleaseItem(
            id=data["id"],
            repo_id=repo_id,
            tag_name=data["tag_name"],
            name=data.get("name"),
            body=data.get("body"),
            draft=data["draft"],
            prerelease=data["prerelease"],
            author_id=author.get("id"),
            author_login=author.get("login"),
            created_at=data["created_at"],
            published_at=data.get("published_at"),
            html_url=data["html_url"],
        )
