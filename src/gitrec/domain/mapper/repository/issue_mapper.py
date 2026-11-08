# src/gitrec/domain/mapper/repository/issue_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.issue_item import IssueItem


class IssueMapper:
    """
    Maps GitHub issue responses into domain issue entities.
    """

    @staticmethod
    def to_issue_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> IssueItem:
        """
        Convert a GitHub issue response into an IssueItem.

        Args:
            data: Raw issue data returned by the GitHub API.
            repo_id: Unique identifier of the repository to which the issue belongs.

        Returns:
            An IssueItem representing the repository issue.
        """
        user = data.get("user") or {}

        return IssueItem(
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
            comments=data["comments"],
            html_url=data["html_url"],
        )
