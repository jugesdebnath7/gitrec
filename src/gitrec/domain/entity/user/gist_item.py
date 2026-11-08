# src/gitrec/domain/entity/user/gist_item.py

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class GistItem(BaseModel):
    """
    Represents a GitHub Gist within the GitRec domain.

    The entity contains gist identity, resource URLs, visibility,
    file information, ownership, metadata, and timestamps used by
    downstream storage and feature-engineering pipelines.

    Attributes:
        id: Unique identifier of the GitHub Gist.
        node_id: Global node identifier of the Gist.
        url: API URL of the Gist resource.
        html_url: Web URL of the Gist.
        git_pull_url: Git URL used to pull the Gist.
        git_push_url: Git URL used to push changes to the Gist.
        forks_url: API URL for forks of the Gist.
        commits_url: API URL for commits associated with the Gist.
        comments_url: API URL for comments associated with the Gist.
        comments: Number of comments associated with the Gist.
        public: Whether the Gist is publicly visible.
        description: Description of the Gist, if available.
        files: Files contained within the Gist.
        owner: GitHub user who owns the Gist, if available.
        created_at: Timestamp when the Gist was created.
        updated_at: Timestamp when the Gist was last updated.
        truncated: Whether the Gist content has been truncated.
    """
    id: str
    node_id: str
    url: str
    html_url: str
    git_pull_url: str
    git_push_url: str
    forks_url: str
    commits_url: str
    comments_url: str
    comments: int
    public: bool
    description: str | None = None
    files: dict[str, Any]
    owner: dict[str, Any] | None = None
    created_at: str
    updated_at: str
    truncated: bool
