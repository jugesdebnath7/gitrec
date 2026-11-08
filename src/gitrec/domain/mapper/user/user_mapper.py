# src/gitrec/domain/mapper/user/user_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.user_item import UserItem
from src.gitrec.domain.mapper.user.event_mapper import EventMapper
from src.gitrec.domain.mapper.user.follower_mapper import FollowerMapper
from src.gitrec.domain.mapper.user.following_mapper import FollowingMapper
from src.gitrec.domain.mapper.user.gist_mapper import GistMapper
from src.gitrec.domain.mapper.user.organization_mapper import OrganizationMapper
from src.gitrec.domain.mapper.user.profile_mapper import ProfileMapper
from src.gitrec.domain.mapper.user.received_event_mapper import ReceivedEventMapper
from src.gitrec.domain.mapper.user.starred_mapper import StarredMapper
from src.gitrec.domain.mapper.user.user_repository_mapper import UserRepositoryMapper


class UserMapper:
    """
    Maps a fully loaded GitHub user resource to a UserItem.

    UserMapper is responsible for assembling the user aggregate.
    Nested user resources are delegated to their specialized mappers.
    """

    @staticmethod
    def to_user_item(resource: dict[str, Any]) -> UserItem:
        """
        Convert a loaded user resource into a UserItem.

        Args:
            resource: Complete user resource containing the core user
                data and any nested resources loaded by the ingestion
                layer.

        Returns:
            A fully mapped UserItem.

        Raises:
            KeyError: If required user fields are missing.
        """
        user_data = resource["user"]

        return UserItem(
            # Core user data
            id=user_data["id"],
            node_id=user_data["node_id"],
            login=user_data["login"],
            avatar_url=user_data.get("avatar_url"),
            html_url=user_data["html_url"],
            type=user_data["type"],
            site_admin=user_data["site_admin"],

            # Nested user resources
            events=[
                EventMapper.to_event_item(
                    event
                )
                for event in resource.get("events", [])
            ],

            followers=[
                FollowerMapper.to_follower_item(
                    follower
                )
                for follower in resource.get("followers", [])
            ],

            following=[
                FollowingMapper.to_following_item(
                    following
                )
                for following in resource.get("following", [])
            ],

            gists=[
                GistMapper.to_gist_item(
                    gist
                )
                for gist in resource.get("gists", [])
            ],

            organizations=[
                OrganizationMapper.to_organization_item(
                    organization
                )
                for organization in resource.get("organizations", [])
            ],

            profile=ProfileMapper.to_profile_item(
                resource.get("profile")
            ),

            received_events=[
                ReceivedEventMapper.to_received_event_item(
                    received_event
                )
                for received_event in resource.get("received_events", [])
            ],

            starred=[
                StarredMapper.to_starred_item(
                    starred
                )
                for starred in resource.get("starred", [])
            ],

            repositories=[
                UserRepositoryMapper.to_user_repository_item(
                    repository
                )
                for repository in resource.get("repositories", [])
            ],
        )