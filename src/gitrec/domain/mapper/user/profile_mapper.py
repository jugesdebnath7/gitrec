# src/gitrec/domain/mapper/user/profile_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.profile_item import ProfileItem


class ProfileMapper:
    """
    Maps GitHub user profile responses into domain profile entities.
    """

    @staticmethod
    def to_profile_item(data: dict[str, Any]) -> ProfileItem:
        """
        Convert a GitHub user profile response into a ProfileItem.

        Args:
            data: Raw user profile data returned by the GitHub API.

        Returns:
            A ProfileItem representing the GitHub user profile.
        """
        return ProfileItem(
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
            name=data.get("name"),
            company=data.get("company"),
            blog=data.get("blog"),
            location=data.get("location"),
            email=data.get("email"),
            hireable=data.get("hireable"),
            bio=data.get("bio"),
            twitter_username=data.get("twitter_username"),
            public_repos=data["public_repos"],
            public_gists=data["public_gists"],
            followers=data["followers"],
            following=data["following"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
        )