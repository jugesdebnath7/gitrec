# src/gitrec/domain/mapper/user/starred_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.starred_item import StarredItem


class StarredMapper:
    """
    Maps GitHub starred repository responses into domain starred entities.
    """

    @staticmethod
    def to_starred_item(data: dict[str, Any]) -> StarredItem:
        """
        Convert a GitHub starred repository response into a StarredItem.

        Args:
            data: Raw starred repository data returned by the GitHub API.

        Returns:
            A StarredItem representing a repository starred by a user.
        """
        return StarredItem(
            id=data["id"],
            node_id=data["node_id"],
            name=data["name"],
            full_name=data["full_name"],
            private=data["private"],
            owner=data["owner"],
            html_url=data["html_url"],
            description=data.get("description"),
            fork=data["fork"],
            url=data["url"],
        )