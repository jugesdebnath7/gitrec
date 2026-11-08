# src/gitrec/domain/entity/repository/release_item.py

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class ReleaseItem(BaseModel):
    """
    Represents a release associated with a repository within the GitRec domain.

    The entity contains release identity, repository association, version
    information, release notes, publication status, author information,
    and timestamps used by downstream storage and feature-engineering
    pipelines.

    Attributes:
        id: GitHub's unique identifier for the release.
        repo_id: Unique identifier of the repository to which the release belongs.
        tag_name: Git tag associated with the release.
        name: Name of the release, if available.
        body: Description or release notes, if available.
        draft: Indicates whether the release is a draft.
        prerelease: Indicates whether the release is marked as a pre-release.
        author_id: GitHub user identifier of the release author, if available.
        author_login: GitHub login of the release author, if available.
        created_at: Timestamp when the release was created.
        published_at: Timestamp when the release was published, if available.
        html_url: Web URL of the release on GitHub.
    """
    id: int
    repo_id: int

    tag_name: str
    name: str | None = None
    body: str | None = None

    draft: bool
    prerelease: bool

    author_id: int | None = None
    author_login: str | None = None

    created_at: datetime
    published_at: datetime | None = None

    html_url: str
