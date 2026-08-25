# src/gitrec/domain/entities/contributor.py

from __future__ import annotations

from pydantic import BaseModel


class ContributorItem(BaseModel):
    """
    Represents a contributor to a repository.

    A contributor represents a user or organization that has contributed
    to a repository and records the number of contributions associated
    with that repository.

    Attributes:
        repo_id: ID of the repository to which the contributor has contributed.
        user_id: GitHub user or organization ID of the contributor.
        login: GitHub login of the contributor.
        contributions: Number of contributions made to the repository.
        type: GitHub account type of the contributor, such as User or Organization.
    """

    repo_id: int
    user_id: int
    login: str
    contributions: int
    type: str