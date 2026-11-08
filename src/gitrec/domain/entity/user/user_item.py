# src/gitrec/domain/entity/user/user_item.py

from __future__ import annotations

from pydantic import BaseModel, Field

from src.gitrec.domain.entity.user.event_item import EventItem
from src.gitrec.domain.entity.user.follower_item import FollowerItem
from src.gitrec.domain.entity.user.following_item import FollowingItem
from src.gitrec.domain.entity.user.gist_item import GistItem
from src.gitrec.domain.entity.user.organization_item import OrganizationItem
from src.gitrec.domain.entity.user.profile_item import ProfileItem
from src.gitrec.domain.entity.user.received_event_item import ReceivedEventItem
from src.gitrec.domain.entity.user.starred_item import StarredItem
from src.gitrec.domain.entity.user.user_repository_item import UserRepositoryItem

class UserItem(BaseModel):
    """
    Represents a GitHub user within the GitRec domain.

    UserItem acts as the aggregate root for a GitHub user. It contains
    the user's core identity and account information together with
    nested resources loaded by the ingestion layer.

    Attributes:
        id: Unique GitHub numeric identifier of the user.
        node_id: Global node identifier of the GitHub user.
        login: GitHub username (login) of the user.
        avatar_url: URL of the user's avatar image, if available.
        html_url: Web URL of the user's GitHub profile.
        type: GitHub account type, such as "User" or "Bot".
        site_admin: Whether the user is a GitHub site administrator.
        events: Public events associated with the user.
        followers: Users following this user.
        following: Users followed by this user.
        gists: Gists created by the user.
        organizations: Organizations associated with the user.
        profile: Extended user profile information, if available.
        received_events: Events received by the user.
        starred: Repositories starred by the user.
        repositories: Repositories owned by or associated with the user.
    """

    # Core user identity
    id: int
    node_id: str
    login: str
    avatar_url: str | None = None
    html_url: str
    type: str
    site_admin: bool = False

    # Nested user resources
    events: list[EventItem] = Field(default_factory=list)
    followers: list[FollowerItem] = Field(default_factory=list)
    following: list[FollowingItem] = Field(default_factory=list)
    gists: list[GistItem] = Field(default_factory=list)
    organizations: list[OrganizationItem] = Field(default_factory=list)
    profile: ProfileItem | None = None
    received_events: list[ReceivedEventItem] = Field(default_factory=list)
    starred: list[StarredItem] = Field(default_factory=list)
    repositories: list[UserRepositoryItem] = Field(default_factory=list)