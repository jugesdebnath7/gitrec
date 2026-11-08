# src/gitrec/domain/entity/user/event_item.py

from __future__ import annotations

from pydantic import BaseModel


class EventItem(BaseModel):
    """
    Represents a GitHub event within the GitRec domain.

    The entity contains event identity, event type, actor information,
    repository information, event-specific payload, and creation
    timestamp used by downstream storage and feature-engineering pipelines.

    Attributes:
        id: Unique GitHub event identifier.
        type: Type of the GitHub event, such as "PushEvent" or "IssuesEvent".
        actor_id: Unique identifier of the GitHub user who triggered the event.
        actor_login: GitHub login of the user who triggered the event.
        repo_id: Unique identifier of the repository associated with the event.
        repo_name: Full name of the repository associated with the event,
            in owner/name format.
        payload: Event-specific payload data returned by the GitHub API.
        created_at: Timestamp when the event was created.
    """
    id: str
    type: str
    actor_id: int
    actor_login: str
    repo_id: int
    repo_name: str
    payload: dict
    created_at: str
