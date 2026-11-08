# src/gitrec/domain/mapper/user/received_event_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.received_event_item import ReceivedEventItem


class ReceivedEventMapper:
    """
    Maps GitHub received event responses into domain received event entities.
    """

    @staticmethod
    def to_received_event_item(data: dict[str, Any]) -> ReceivedEventItem:
        """
        Convert a GitHub received event response into a ReceivedEventItem.

        Args:
            data: Raw received event data returned by the GitHub API.

        Returns:
            A ReceivedEventItem representing the GitHub received event.
        """
        actor = data["actor"]
        repo = data["repo"]

        return ReceivedEventItem(
            id=data["id"],
            type=data["type"],
            actor_id=actor["id"],
            actor_login=actor["login"],
            actor_url=actor["url"],
            repo_id=repo["id"],
            repo_name=repo["name"],
            repo_url=repo["url"],
            created_at=data["created_at"],
        )