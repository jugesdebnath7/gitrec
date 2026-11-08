# src/gitrec/domain/mapper/user/event_mapper.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.user.event_item import EventItem


class EventMapper:
    """
    Maps GitHub event responses into domain event entities.
    """

    @staticmethod
    def to_event_item(data: dict[str, Any]) -> EventItem:
        """
        Convert a GitHub event response into an EventItem.

        Args:
            data: Raw event data returned by the GitHub API.

        Returns:
            An EventItem representing the GitHub event.
        """
        actor = data.get("actor") or {}
        repo = data.get("repo") or {}

        return EventItem(
            id=data["id"],
            type=data["type"],
            actor_id=actor["id"],
            actor_login=actor["login"],
            repo_id=repo["id"],
            repo_name=repo["name"],
            payload=data.get("payload", {}),
            created_at=data["created_at"],
        )