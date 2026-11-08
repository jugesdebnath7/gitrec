# src/gitrec/domain/entity/repository/commit_item.py

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class CommitItem(BaseModel):
    """
    Represents a commit associated with a repository within the GitRec domain.

    The entity contains commit identity, repository association, message,
    author and committer information, timestamps, and the GitHub resource
    URL used by downstream storage and feature-engineering pipelines.

    Attributes:
        sha: Unique SHA identifier of the commit.
        repo_id: Unique identifier of the repository to which the commit belongs.
        message: Commit message describing the changes.
        author_id: GitHub user ID associated with the commit author, if available.
        author_login: GitHub login associated with the commit author, if available.
        committer_id: GitHub user ID associated with the commit committer, if available.
        committer_login: GitHub login associated with the commit committer, if available.
        authored_at: Timestamp when the commit was authored, if available.
        committed_at: Timestamp when the commit was committed, if available.
        html_url: Web URL of the commit on GitHub.
    """
    sha: str
    repo_id: int
    message: str

    author_id: int | None
    author_login: str | None

    committer_id: int | None
    committer_login: str | None

    authored_at: datetime | None
    committed_at: datetime | None

    html_url: str
