# src/gitrec/domain/entities/commit.py

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class CommitItem(BaseModel):
    """
    Represents a commit associated with a repository.

    A commit records a change made to a repository, including its
    identity, message, author and committer information, and timestamps.

    Attributes:
        sha: Unique SHA identifier of the commit.
        repo_id: ID of the repository to which the commit belongs.
        message: Commit message describing the changes.
        author_id: GitHub user ID of the commit author, if available.
        author_login: GitHub login of the commit author, if available.
        committer_id: GitHub user ID of the committer, if available.
        committer_login: GitHub login of the committer, if available.
        authored_at: Timestamp when the commit was authored, if available.
        committed_at: Timestamp when the commit was committed, if available.
        html_url: URL of the commit on GitHub.
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