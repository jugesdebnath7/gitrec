# src/gitrec/domain/mapper/user/gist_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.gist_item import GistItem


class GistMapper:
    """
    Maps GitHub Gist responses into domain Gist entities.
    """

    @staticmethod
    def to_gist_item(data: dict[str, Any]) -> GistItem:
        """
        Convert a GitHub Gist response into a GistItem.

        Args:
            data: Raw Gist data returned by the GitHub API.

        Returns:
            A GistItem representing the GitHub Gist.
        """
        return GistItem(
            id=data["id"],
            node_id=data["node_id"],
            url=data["url"],
            html_url=data["html_url"],
            git_pull_url=data["git_pull_url"],
            git_push_url=data["git_push_url"],
            forks_url=data["forks_url"],
            commits_url=data["commits_url"],
            comments_url=data["comments_url"],
            comments=data["comments"],
            public=data["public"],
            description=data.get("description"),
            files=data.get("files", {}),
            owner=data.get("owner"),
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            truncated=data["truncated"],
        )