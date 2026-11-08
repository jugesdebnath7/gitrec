# src/gitrec/domain/entity/repository/tag_item.py

from __future__ import annotations

from pydantic import BaseModel


class TagItem(BaseModel):
    """
    Represents a tag in a repository within the GitRec domain.

    A tag is a named reference to a specific point in a repository's
    history and is commonly used to mark releases or important
    milestones.

    Attributes:
        repo_id: Unique identifier of the repository that contains the tag.
        tag_name: Name of the tag.
        commit_sha: SHA of the commit referenced by the tag.
        created_at: Timestamp indicating when the tag was created, if available.
    """
    repo_id: int
    tag_name: str
    commit_sha: str
    created_at: str

