# src/gitrec/ingestion/github/domain/repository.py

"""
Repository domain models.

Defines the domain model representing GitHub repository metadata used
throughout the application.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class RepoItem(BaseModel):
    """
    Represents a GitHub repository within the application domain.
    """

    github_id: int = Field(
        description="Unique GitHub repository identifier.",
    )

    owner: str = Field(
        description="Repository owner login.",
    )

    name: str = Field(
        description="Repository name.",
    )

    full_name: str = Field(
        description="Repository full name including the owner.",
    )

    description: str | None = Field(
        default=None,
        description="Repository description.",
    )

    visibility: str | None = Field(
        default=None,
        description="Repository visibility.",
    )

    default_branch: str | None = Field(
        default=None,
        description="Default branch name.",
    )

    language: str | None = Field(
        default=None,
        description="Primary programming language.",
    )

    stars: int = Field(
        default=0,
        description="Repository star count.",
    )

    forks: int = Field(
        default=0,
        description="Repository fork count.",
    )

    watchers: int = Field(
        default=0,
        description="Repository watcher count.",
    )

    open_issues: int = Field(
        default=0,
        description="Number of open issues.",
    )

    topics: list[str] = Field(
        default_factory=list,
        description="Repository topics.",
    )