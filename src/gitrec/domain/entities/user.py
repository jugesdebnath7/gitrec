# src/gitrec/ingestion/github/users.py

from __future__ import annotations
from pydantic import BaseModel


class UserItem(BaseModel):
    """
    Represents a GitHub user.

    A user includes identifying information, profile URLs, account type,
    and administrator status.

    Attributes:
        id: GitHub's unique numeric identifier for the user.
        node_id: GitHub's unique node identifier for the user.
        login: GitHub username (login) of the user.
        avatar_url: URL of the user's avatar image, if available.
        html_url: URL of the user's GitHub profile.
        type: GitHub account type, such as "User" or "Bot".
        site_admin: Whether the user is a GitHub site administrator.
    """
    id: int
    node_id: str

    login: str

    avatar_url: str | None
    html_url: str

    type: str

    site_admin: bool
