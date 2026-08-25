# src/gitrec/domain/entities/branch.py

from __future__ import annotations

from pydantic import BaseModel


class BranchItem(BaseModel):
    """
    Represents a repository branch.

    A branch identifies a named line of development within a repository
    and points to the commit currently at the tip of that branch.

    Attributes:
        repo_id: ID of the repository to which the branch belongs.
        name: Name of the branch.
        commit_sha: SHA of the commit currently at the tip of the branch.
        protected: Whether branch protection is enabled.
    """
    repo_id: int
    name: str
    commit_sha: str
    protected: bool = False