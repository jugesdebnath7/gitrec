# src/gitrec/domain/mapper/user/following_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.following_item import FollowingItem


class FollowingMapper:
    """
    Maps GitHub following responses into domain following entities.
    """

    @staticmethod
    def to_following_item(data: dict[str, Any]) -> FollowingItem:
        """
        Convert a GitHub following response into a FollowingItem.

        Args:
            data: Raw following data returned by the GitHub API.

        Returns:
            A FollowingItem representing a user followed by another user.
        """
        return FollowingItem(
            login=data["login"],
            id=data["id"],
            node_id=data["node_id"],
            avatar_url=data["avatar_url"],
            gravatar_id=data["gravatar_id"],
            url=data["url"],
            html_url=data["html_url"],
            followers_url=data["followers_url"],
            following_url=data["following_url"],
            gists_url=data["gists_url"],
            starred_url=data["starred_url"],
            subscriptions_url=data["subscriptions_url"],
            organizations_url=data["organizations_url"],
            repos_url=data["repos_url"],
            events_url=data["events_url"],
            received_events_url=data["received_events_url"],
            type=data["type"],
            site_admin=data["site_admin"],
        )