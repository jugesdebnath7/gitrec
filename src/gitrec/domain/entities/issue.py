# src/gitrec/domain/entities/issue.py

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class IssueItem(BaseModel):
    """
    Represents an issue associated with a repository.

    An issue records a problem, task, or discussion within a repository,
    including its state, author, timestamps, and associated metadata.

    Attributes:
        id: GitHub's unique identifier for the issue.
        number: Repository-specific issue number.
        repo_id: ID of the repository to which the issue belongs.
        title: Title of the issue.
        body: Detailed description or content of the issue, if available.
        state: Current state of the issue, such as open or closed.
        user_id: GitHub user ID of the issue author.
        user_login: GitHub login of the issue author.
        created_at: Timestamp when the issue was created.
        updated_at: Timestamp when the issue was last updated.
        closed_at: Timestamp when the issue was closed, if applicable.
        comments: Number of comments associated with the issue.
        html_url: URL of the issue on GitHub.
    """

    id: int
    number: int

    repo_id: int

    title: str
    body: str | None

    state: str

    user_id: int
    user_login: str

    created_at: datetime
    updated_at: datetime
    closed_at: datetime | None

    comments: int

    html_url: str