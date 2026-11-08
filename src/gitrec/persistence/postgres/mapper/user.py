# scr/gitrec/persistence/postgres/mapper/user.py

"""Map user domain aggregates to database-ready records.

This module transforms UserItem aggregates into dictionaries grouped by
their destination persistence resources.

It performs no database I/O and does not manage connections or transactions.
Each nested resource has its own mapping method to keep transformations
focused and independently testable.
"""

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.user_item import UserItem


Record = dict[str, Any]
Records = dict[str, list[Record]]


class UserMapper:
    """Flatten user aggregates into resource-specific record dictionaries."""

    def flatten(
        self,
        users: list[UserItem],
    ) -> Records:
        """Convert users and nested resources into database-ready records.

        Args:
            users: User aggregates to flatten.

        Returns:
            A dictionary containing one list per persistence resource.
            Empty input returns the same dictionary structure with empty lists.

        Raises:
            TypeError: If users is not a list of UserItem instances.
        """
        self._validate_users(users)

        records: Records = {
            "users": [],
            "events": [],
            "followers": [],
            "following": [],
            "gists": [],
            "organizations": [],
            "profiles": [],
            "received_events": [],
            "starred": [],
            "user_repositories": [],
        }

        for user in users:
            records["users"].append(
                self._map_user(user)
            )

            records["profiles"].extend(
                self._map_profile(user)
            )

            records["events"].extend(
                self._map_events(user)
            )

            records["followers"].extend(
                self._map_followers(user)
            )

            records["following"].extend(
                self._map_following(user)
            )

            records["gists"].extend(
                self._map_gists(user)
            )

            records["organizations"].extend(
                self._map_organizations(user)
            )

            records["received_events"].extend(
                self._map_received_events(user)
            )

            records["starred"].extend(
                self._map_starred(user)
            )

            records["user_repositories"].extend(
                self._map_repositories(user)
            )

        return records

    @staticmethod
    def _validate_users(users: list[UserItem]) -> None:
        """Validate that the input is a list of UserItem instances."""
        if not isinstance(users, list):
            raise TypeError(
                "Expected a list of UserItem instances, "
                f"got {type(users).__name__}."
            )

        for index, user in enumerate(users):
            if not isinstance(user, UserItem):
                raise TypeError(
                    f"Expected UserItem at index {index}, "
                    f"got {type(user).__name__}."
                )
            
    @staticmethod
    def _map_user(user: UserItem) -> Record:
        """Map core user identity and account information."""
        return {
            "id": user.id,
            "node_id": user.node_id,
            "login": user.login,
            "avatar_url": user.avatar_url,
            "html_url": user.html_url,
            "type": user.type,
            "site_admin": user.site_admin,
        }

    @staticmethod
    def _map_events(user: UserItem) -> list[Record]:
        """Map the user's public events."""
        return [
            {
                "id": event.id,
                "type": event.type,
                "actor_id": event.actor_id,
                "actor_login": event.actor_login,
                "repo_id": event.repo_id,
                "repo_name": event.repo_name,
                "payload": event.payload,
                "created_at": event.created_at,
            }
            for event in user.events
        ]

    @staticmethod
    def _map_followers(user: UserItem) -> list[Record]:
        """Map users following this user."""
        return [
            {
                "login": follower.login,
                "id": follower.id,
                "node_id": follower.node_id,
                "avatar_url": follower.avatar_url,
                "gravatar_id": follower.gravatar_id,
                "url": follower.url,
                "html_url": follower.html_url,
                "followers_url": follower.followers_url,
                "following_url": follower.following_url,
                "gists_url": follower.gists_url,
                "starred_url": follower.starred_url,
                "subscriptions_url": follower.subscriptions_url,
                "organizations_url": follower.organizations_url,
                "repos_url": follower.repos_url,
                "events_url": follower.events_url,
                "received_events_url": follower.received_events_url,
                "type": follower.type,
                "site_admin": follower.site_admin,
            }
            for follower in user.followers
        ]

    @staticmethod
    def _map_following(user: UserItem) -> list[Record]:
        """Map users followed by this user."""
        return [
            {
                "login": following.login,
                "id": following.id,
                "node_id": following.node_id,
                "avatar_url": following.avatar_url,
                "gravatar_id": following.gravatar_id,
                "url": following.url,
                "html_url": following.html_url,
                "followers_url": following.followers_url,
                "following_url": following.following_url,
                "gists_url": following.gists_url,
                "starred_url": following.starred_url,
                "subscriptions_url": following.subscriptions_url,
                "organizations_url": following.organizations_url,
                "repos_url": following.repos_url,
                "events_url": following.events_url,
                "received_events_url": following.received_events_url,
                "type": following.type,
                "site_admin": following.site_admin,
            }
            for following in user.following
        ]

    @staticmethod
    def _map_gists(user: UserItem) -> list[Record]:
        """Map gists created by the user."""
        return [
            {
                "id": gist.id,
                "node_id": gist.node_id,
                "url": gist.url,
                "html_url": gist.html_url,
                "git_pull_url": gist.git_pull_url,
                "git_push_url": gist.git_push_url,
                "forks_url": gist.forks_url,
                "commits_url": gist.commits_url,
                "comments_url": gist.comments_url,
                "comments": gist.comments,
                "public": gist.public,
                "description": gist.description,
                "files": gist.files,
                "owner": gist.owner,
                "created_at": gist.created_at,
                "updated_at": gist.updated_at,
                "truncated": gist.truncated,
            }
            for gist in user.gists
        ]

    @staticmethod
    def _map_organizations(user: UserItem) -> list[Record]:
        """Map organizations associated with the user."""
        return [
            {
                "login": organization.login,
                "id": organization.id,
                "node_id": organization.node_id,
                "avatar_url": organization.avatar_url,
                "gravatar_id": organization.gravatar_id,
                "url": organization.url,
                "html_url": organization.html_url,
            }
            for organization in user.organizations
        ]

    @staticmethod
    def _map_profile(user: UserItem) -> list[Record]:
        """Map the user's optional extended profile."""
        if user.profile is None:
            return []
        profile = user.profile

        return [
            {
                "login": profile.login,
                "id": profile.id,
                "node_id": profile.node_id,
                "avatar_url": profile.avatar_url,
                "gravatar_id": profile.gravatar_id,
                "url": profile.url,
                "html_url": profile.html_url,
                "followers_url": profile.followers_url,
                "following_url": profile.following_url,
                "gists_url": profile.gists_url,
                "starred_url": profile.starred_url,
                "subscriptions_url": profile.subscriptions_url,
                "organizations_url": profile.organizations_url,
                "repos_url": profile.repos_url,
                "events_url": profile.events_url,
                "received_events_url": profile.received_events_url,
                "type": profile.type,
                "site_admin": profile.site_admin,
                "name": profile.name,
                "company": profile.company,
                "blog": profile.blog,
                "location": profile.location,
                "email": profile.email,
                "hireable": profile.hireable,
                "bio": profile.bio,
                "twitter_username": profile.twitter_username,
                "public_repos": profile.public_repos,
                "public_gists": profile.public_gists,
                "followers": profile.followers,
                "following": profile.following,
                "created_at": profile.created_at,
                "updated_at": profile.updated_at,
            }
        ]

    @staticmethod
    def _map_received_events(user: UserItem) -> list[Record]:
        """Map events received by the user."""
        return [
            {
                "id": received_event.id,
                "type": received_event.type,
                "actor_id": received_event.actor_id,
                "actor_login": received_event.actor_login,
                "actor_url": received_event.actor_url,
                "repo_id": received_event.repo_id,
                "repo_name": received_event.repo_name,
                "repo_url": received_event.repo_url,
                "created_at": received_event.created_at,
            }
            for received_event in user.received_events
        ]

    @staticmethod
    def _map_starred(user: UserItem) -> list[Record]:
        """Map repositories starred by the user."""
        return [
            {
                "id": starred.id,
                "node_id": starred.node_id,
                "name": starred.name,
                "full_name": starred.full_name,
                "private": starred.private,
                "owner": starred.owner,
                "html_url": starred.html_url,
                "description": starred.description,
                "fork": starred.fork,
                "url": starred.url,
            }
            for starred in user.starred
        ]

    @staticmethod
    def _map_repositories(user: UserItem) -> list[Record]:
        """Map repositories associated with the user."""
        return [
            {
                "id": repository.id,
                "node_id": repository.node_id,
                "name": repository.name,
                "full_name": repository.full_name,
                "private": repository.private,
                "owner": repository.owner,
                "html_url": repository.html_url,
                "description": repository.description,
                "fork": repository.fork,
                "url": repository.url,
            }
            for repository in user.repositories
        ]
