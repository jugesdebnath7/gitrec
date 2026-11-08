# src/gitrec/domain/mapper/repository/commit_mapper.py

from __future__ import annotations

from datetime import datetime
from typing import Any

from src.gitrec.domain.entity.repository.commit_item import CommitItem


class CommitMapper:
    """
    Maps GitHub commit responses into domain commit entities.
    """

    @staticmethod
    def to_commit_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> CommitItem:
        """
        Convert a GitHub commit response into a CommitItem.

        Args:
            data: Raw commit data returned by the GitHub API.
            repo_id: Unique identifier of the repository to which the commit belongs.

        Returns:
            A CommitItem representing the repository commit.
        """
        author = data.get("author") or {}
        committer = data.get("committer") or {}

        commit_data = data.get("commit") or {}
        author_data = commit_data.get("author") or {}
        committer_data = commit_data.get("committer") or {}

        return CommitItem(
            sha=data["sha"],
            repo_id=repo_id,
            message=commit_data.get("message", ""),

            author_id=author.get("id"),
            author_login=author.get("login"),

            committer_id=committer.get("id"),
            committer_login=committer.get("login"),

            authored_at=(
                datetime.fromisoformat(
                    author_data["date"].replace("Z", "+00:00")
                )
                if author_data.get("date")
                else None
            ),
            committed_at=(
                datetime.fromisoformat(
                    committer_data["date"].replace("Z", "+00:00")
                )
                if committer_data.get("date")
                else None
            ),

            html_url=data["html_url"],
        )
