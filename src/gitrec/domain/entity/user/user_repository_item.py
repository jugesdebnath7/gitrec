# src/gitrec/domain/entity/user/user_repository_item.py

from __future__ import annotations

from pydantic import BaseModel


class UserRepositoryItem(BaseModel):
    """
    Represents a GitHub repository owned by a user within the GitRec domain.

    The entity contains repository identity, ownership, metadata, repository
    state, and GitHub resource URLs used by downstream storage and
    feature-engineering pipelines.

    Attributes:
        id: Unique GitHub repository identifier.
        node_id: Global node identifier of the GitHub repository.
        name: Name of the repository.
        full_name: Full name of the repository in owner/name format.
        private: Whether the repository is private.
        owner: Owner of the repository, represented as a dictionary
            containing GitHub user or organization information.
        html_url: Web URL of the repository on GitHub.
        description: Description of the repository, if available.
        fork: Whether the repository is a fork of another repository.
        url: API URL of the repository resource.
    """
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: dict
    html_url: str
    description: str | None
    fork: bool
    url: str