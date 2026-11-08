# src/gitrec/domain/mapper/repository/readme_mapper.py

from __future__ import annotations

import base64
from typing import Any

from src.gitrec.domain.entity.repository.readme_item import ReadmeItem


class ReadmeMapper:
    """
    Maps GitHub README responses into domain README entities.
    """

    @staticmethod
    def to_readme_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> ReadmeItem:
        """
        Convert a GitHub README response into a ReadmeItem.

        Args:
            data: Raw README data returned by the GitHub API.
            repo_id: Unique identifier of the repository containing the README.

        Returns:
            A ReadmeItem representing the repository README.
        """
        content = data.get("content", "")
        encoding = data.get("encoding", "")

        if encoding.lower() == "base64":
            content = base64.b64decode(content).decode("utf-8")

        return ReadmeItem(
            repo_id=repo_id,
            content=content,
        )
