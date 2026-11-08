# src/gitrec/domain/entity/user/profile_item.py

from __future__ import annotations

from pydantic import BaseModel


class ProfileItem(BaseModel):
    """
    Represents a GitHub user profile within the GitRec domain.

    The entity contains user identity, profile information, account
    metadata, activity statistics, and GitHub resource URLs used by
    downstream storage and feature-engineering pipelines.

    Attributes:
        login: GitHub login/username of the user.
        id: Unique GitHub user identifier.
        node_id: Global node identifier of the GitHub user.
        avatar_url: URL of the user's GitHub avatar.
        gravatar_id: Gravatar identifier associated with the user.
        url: API URL of the user's GitHub resource.
        html_url: Web URL of the user's GitHub profile.
        followers_url: API URL for the user's followers.
        following_url: API URL for users followed by the user.
        gists_url: API URL for the user's Gists.
        starred_url: API URL for repositories starred by the user.
        subscriptions_url: API URL for the user's subscriptions.
        organizations_url: API URL for organizations associated with the user.
        repos_url: API URL for repositories owned by the user.
        events_url: API URL for events performed by the user.
        received_events_url: API URL for events received by the user.
        type: Type of the GitHub account, typically "User".
        site_admin: Whether the user is a GitHub site administrator.
        name: Display name of the user, if available.
        company: Company associated with the user, if available.
        blog: Blog or website URL associated with the user, if available.
        location: Location provided by the user, if available.
        email: Public email address provided by the user, if available.
        hireable: Whether the user is available for hire, if specified.
        bio: Biography or description provided by the user, if available.
        twitter_username: Twitter/X username associated with the user, if available.
        public_repos: Number of public repositories owned by the user.
        public_gists: Number of public Gists owned by the user.
        followers: Number of users following the user.
        following: Number of users followed by the user.
        created_at: Timestamp when the GitHub account was created.
        updated_at: Timestamp when the profile was last updated.
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

    name: str | None
    company: str | None
    blog: str | None
    location: str | None
    email: str | None
    hireable: bool | None
    bio: str | None
    twitter_username: str | None

    public_repos: int
    public_gists: int
    followers: int
    following: int

    created_at: str
    updated_at: str