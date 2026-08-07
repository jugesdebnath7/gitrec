# src/gitrec/ingestion/github/mapper/repositroy.py

"""
Repository mapping utilities.

This module transforms raw GitHub repository payloads produced by the
loader into repository domain models.
"""

from __future__ import annotations

from typing import Any

from gitrec.ingestion.github.entities.repository import RepoItem


def map_repository(data: dict[str, Any]) -> RepoItem:
    """
    Convert a raw GitHub repository payload into a repository domain model.

    Args:
        data:
            Composite payload returned by ``RepositoryLoader``.

    Returns:
        Repository domain model.

    Raises:
        ValueError:
            If the primary repository payload is unavailable.
    """
    repo = data.get("repo")

    if not isinstance(repo, dict):
        raise ValueError(
            "Repository metadata is unavailable."
        )

    return RepoItem(
        github_id=repo["id"],
        owner=repo["owner"]["login"],
        name=repo["name"],
        full_name=repo["full_name"],
        description=repo.get("description"),
        visibility=repo.get("visibility"),
        default_branch=repo.get("default_branch"),
        language=repo.get("language"),
        stars=repo.get("stargazers_count", 0),
        forks=repo.get("forks_count", 0),
        watchers=repo.get("watchers_count", 0),
        open_issues=repo.get("open_issues_count", 0),
        topics=data.get("topics", []),
    )