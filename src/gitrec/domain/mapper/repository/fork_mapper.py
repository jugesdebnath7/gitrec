# src/gitrec/domain/mapper/repository/fork_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.fork_item import ForkItem


class ForkMapper:
    """
    Maps GitHub fork responses into domain fork entities.
    """

    @staticmethod
    def to_fork_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> ForkItem:
        """
        Convert a GitHub fork response into a ForkItem.

        Args:
            data: Raw fork data returned by the GitHub API.
            repo_id: Unique identifier of the original repository.

        Returns:
            A ForkItem representing the repository fork.
        """
        owner = data.get("owner") or {}

        return ForkItem(
            repo_id=repo_id,
            fork_id=data["id"],
            owner_id=owner["id"],
            owner_login=owner["login"],
            created_at=data["created_at"],
        )

