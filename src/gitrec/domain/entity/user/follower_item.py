# src/gitrec/domain/entity/user/follower_item.py

from __future__ import annotations

from pydantic import BaseModel


class FollowerItem(BaseModel):
    """
    Represents a GitHub follower within the GitRec domain.

    The entity contains the follower's identity, profile information,
    account type, administrator status, and GitHub resource URLs used
    by downstream storage and feature-engineering pipelines.

    Attributes:
        login: GitHub login/username of the follower.
        id: Unique GitHub user identifier.
        node_id: Global node identifier of the GitHub user.
        avatar_url: URL of the follower's GitHub avatar.
        gravatar_id: Gravatar identifier associated with the follower.
        url: API URL of the follower's GitHub user resource.
        html_url: Web URL of the follower's GitHub profile.
        followers_url: API URL for the follower's followers.
        following_url: API URL for the users followed by the follower.
        gists_url: API URL for the follower's gists.
        starred_url: API URL for repositories starred by the follower.
        subscriptions_url: API URL for the follower's repository subscriptions.
        organizations_url: API URL for organizations associated with the follower.
        repos_url: API URL for repositories owned by the follower.
        events_url: API URL for events performed by the follower.
        received_events_url: API URL for events received by the follower.
        type: Type of the GitHub account, typically "User" or "Bot".
        site_admin: Whether the follower is a GitHub site administrator.
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