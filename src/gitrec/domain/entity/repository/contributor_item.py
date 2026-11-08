# src/gitrec/domain/entity/repository/contributor_item.py

from __future__ import annotations

from pydantic import BaseModel


class ContributorItem(BaseModel):
    """
    Represents a contributor to a repository within the GitRec domain.

    The entity contains the contributor's identity, account type,
    repository association, and contribution count used by downstream
    storage and feature-engineering pipelines.

    Attributes:
        repo_id: Unique identifier of the repository to which the contributor
            has contributed.
        user_id: Unique GitHub user or organization identifier of the contributor.
        login: GitHub login of the contributor.
        contributions: Number of contributions made to the repository.
        type: GitHub account type of the contributor, such as "User" or
            "Organization".
    """
    repo_id: int
    user_id: int
    login: str
    contributions: int
    type: str
