# src/gitrec/domain/mapper/repository/pull_request_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.pull_request_item import PullRequestItem


class PullRequestMapper:
    """
    Maps GitHub pull request responses into domain pull request entities.
    """

    @staticmethod
    def to_pull_request_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> PullRequestItem:
        """
        Convert a GitHub pull request response into a PullRequestItem.

        Args:
            data: Raw pull request data returned by the GitHub API.
            repo_id: Unique identifier of the repository to which the
                pull request belongs.

        Returns:
            A PullRequestItem representing the repository pull request.
        """
        user = data.get("user") or {}

        return PullRequestItem(
            id=data["id"],
            number=data["number"],
            repo_id=repo_id,
            title=data["title"],
            body=data.get("body"),
            state=data["state"],
            user_id=user["id"],
            user_login=user["login"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            closed_at=data.get("closed_at"),
            merged_at=data.get("merged_at"),
            html_url=data["html_url"],
        )
