# src/gitrec/domain/mapper/repository/branch_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.branch_item import BranchItem


class BranchMapper:
    """
    Maps GitHub branch responses into domain branch entities.
    """

    @staticmethod
    def to_branch_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> BranchItem:
        """
        Convert a GitHub branch response into a BranchItem.

        Args:
            data: Raw branch data returned by the GitHub API.
            repo_id: Unique identifier of the repository to which the branch belongs.

        Returns:
            A BranchItem representing the repository branch.
        """
        return BranchItem(
            repo_id=repo_id,
            name=data["name"],
            commit_sha=data["commit"]["sha"],
            protected=data.get("protected", False),
        )
