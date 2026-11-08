# src/gitrec/domain/entity/repository/readme_item.py

from __future__ import annotations

from pydantic import BaseModel


class ReadmeItem(BaseModel):
    """
    Represents the README file of a repository within the GitRec domain.

    The entity contains the repository association and README content
    used by downstream storage and feature-engineering pipelines.

    Attributes:
        repo_id: Unique identifier of the repository that has the README file.
        content: Content of the README file in plain text or Markdown format.
    """
    repo_id: int
    content: str
