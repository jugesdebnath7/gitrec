# src/gitrec/domain/entity/user/organization_item.py

from __future__ import annotations

from pydantic import BaseModel


class OrganizationItem(BaseModel):
    """
    Represents a GitHub organization associated with a user within the
    GitRec domain.

    The entity contains organization identity, profile information,
    and GitHub resource URLs used by downstream storage and
    feature-engineering pipelines.

    Attributes:
        login: GitHub login/username of the organization.
        id: Unique GitHub organization identifier.
        node_id: Global node identifier of the GitHub organization.
        avatar_url: URL of the organization's GitHub avatar.
        gravatar_id: Gravatar identifier associated with the organization.
        url: API URL of the organization's GitHub resource.
        html_url: Web URL of the organization's GitHub profile.
    """
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str