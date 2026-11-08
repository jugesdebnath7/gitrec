# src/gitrec/domain/entity/repository/fork_item.py

from __future__ import annotations

from pydantic import BaseModel


class ForkItem(BaseModel):
    """
    Represents a fork of a repository within the GitRec domain.

    The entity contains the association between the original repository
    and its fork, the fork owner's identity, and the fork creation
    timestamp used by downstream storage and feature-engineering pipelines.

    Attributes:
        repo_id: Unique identifier of the original repository that was forked.
        fork_id: Unique identifier of the forked repository.
        owner_id: GitHub user or organization identifier of the fork owner.
        owner_login: GitHub login of the fork owner.
        created_at: Timestamp indicating when the fork was created.
    """
    repo_id: int
    fork_id: int
    owner_id: int
    owner_login: str
    created_at: str

