# src/gitrec/domain/entity/user/following_item.py

from __future__ import annotations

from pydantic import BaseModel


class FollowingItem(BaseModel):
    """
    Represents a GitHub user followed by another user within the GitRec domain.

    The entity contains the followed user's identity, profile information,
    account type, administrator status, and GitHub resource URLs used by
    downstream storage and feature-engineering pipelines.

    Attributes:
        login: GitHub login/username of the followed user.
        id: Unique GitHub user identifier.
        node_id: Global node identifier of the GitHub user.
        avatar_url: URL of the followed user's GitHub avatar.
        gravatar_id: Gravatar identifier associated with the followed user.
        url: API URL of the followed user's GitHub user resource.
        html_url: Web URL of the followed user's GitHub profile.
        followers_url: API URL for the followed user's followers.
        following_url: API URL for users followed by the followed user.
        gists_url: API URL for the followed user's gists.
        starred_url: API URL for repositories starred by the followed user.
        subscriptions_url: API URL for the followed user's repository subscriptions.
        organizations_url: API URL for organizations associated with the followed user.
        repos_url: API URL for repositories owned by the followed user.
        events_url: API URL for events performed by the followed user.
        received_events_url: API URL for events received by the followed user.
        type: Type of the GitHub account, typically "User" or "Bot".
        site_admin: Whether the followed user is a GitHub site administrator.
    """
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool