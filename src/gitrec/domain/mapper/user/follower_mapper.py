# src/gitrec/domain/mapper/user/follower_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.follower_item import FollowerItem


class FollowerMapper:
    """
    Maps GitHub follower responses into domain follower entities.
    """

    @staticmethod
    def to_follower_item(data: dict[str, Any]) -> FollowerItem:
        """
        Convert a GitHub follower response into a FollowerItem.

        Args:
            data: Raw follower data returned by the GitHub API.

        Returns:
            A FollowerItem representing the GitHub follower.
        """
        return FollowerItem(
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