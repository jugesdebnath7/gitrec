# src/gitrec/domain/entity/repository/branch_item.py

from __future__ import annotations

from pydantic import BaseModel


class BranchItem(BaseModel):
    """
    Represents a repository branch within the GitRec domain.

    The entity contains branch identity, its association with a repository,
    the commit currently at the branch tip, and branch protection status
    used by downstream storage and feature-engineering pipelines.

    Attributes:
        repo_id: Unique identifier of the repository to which the branch belongs.
        name: Name of the branch.
        commit_sha: SHA of the commit currently at the tip of the branch.
        protected: Indicates whether branch protection is enabled.
    """
    repo_id: int
    name: str
    commit_sha: str
    protected: bool = False
