# src/gitrec/domain/mapper/user/user_repository_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.user_repository_item import UserRepositoryItem


class UserRepositoryMapper:
    """
    Maps GitHub user repository responses into domain user repository entities.
    """

    @staticmethod
    def to_user_repository_item(data: dict[str, Any]) -> UserRepositoryItem:
        """
        Convert a GitHub user repository response into a UserRepository.

        Args:
            data: Raw repository data returned by the GitHub API.

        Returns:
            A UserRepository representing a repository owned by a user.
        """
        return UserRepositoryItem(
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