# src/gitrec/domain/entities/pull_request.py

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class PullRequestItem(BaseModel):
    """
    Represents a pull request associated with a repository.

    A pull request records a proposed change to a repository, including
    its state, author, timestamps, and merge status.

    Attributes:
        id: GitHub's unique identifier for the pull request.
        number: Repository-specific pull request number.
        repo_id: ID of the repository to which the pull request belongs.
        title: Title of the pull request.
        body: Detailed description or content of the pull request,
            if available.
        state: Current state of the pull request, such as open or closed.
        user_id: GitHub user ID of the pull request author.
        user_login: GitHub login of the pull request author.
        created_at: Timestamp when the pull request was created.
        updated_at: Timestamp when the pull request was last updated.
        closed_at: Timestamp when the pull request was closed, if applicable.
        merged_at: Timestamp when the pull request was merged, if applicable.
        html_url: URL of the pull request on GitHub.
    """

    id: int
    number: int

    repo_id: int

    title: str
    body: str | None = None

    state: str

    user_id: int
    user_login: str

    created_at: datetime
    updated_at: datetime
    closed_at: datetime | None = None
    merged_at: datetime | None = None

    html_url: str