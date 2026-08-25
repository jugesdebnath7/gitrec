# src/gitrec/domain/entities/repository.py

from __future__ import annotations

from pydantic import BaseModel, Field


class RepoItem(BaseModel):
    """
    Represents a GitHub repository within the GitRec domain.

    The entity contains repository identity, ownership, metadata,
    activity statistics, and repository state used by downstream
    storage and feature-engineering pipelines.

    Attributes:
        id: Unique GitHub repository identifier.
        owner: GitHub login of the repository owner.
        name: Repository name.
        full_name: Full repository name in owner/name format.
        description: Repository description, if available.
        visibility: Repository visibility, if available.
        default_branch: Name of the repository's default branch,
            if available.
        language: Primary programming language of the repository,
            if available.
        stars: Number of stars received by the repository.
        forks: Number of forks of the repository.
        watchers: Number of users watching the repository.
        open_issues: Number of open issues associated with the repository.
        topics: Topics associated with the repository.
        fork: Whether the repository is a fork.
        archived: Whether the repository has been archived.
        disabled: Whether the repository is disabled.
    """
    id: int
    owner: str
    name: str
    full_name: str

    description: str | None = None
    visibility: str | None = None
    default_branch: str | None = None
    language: str | None = None

    stars: int = 0
    forks: int = 0
    watchers: int = 0
    open_issues: int = 0

    topics: list[str]

    fork: bool = False
    archived: bool = False
    disabled: bool = False