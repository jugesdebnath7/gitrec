# src/gitrec/domain/entity/user/received_event_item.py

from __future__ import annotations

from pydantic import BaseModel


class ReceivedEventItem(BaseModel):
    """
    Represents a GitHub event received by a user within the GitRec domain.

    The entity contains event identity, event type, actor information,
    repository information, resource URLs, and creation timestamp used
    by downstream storage and feature-engineering pipelines.

    Attributes:
        id: Unique GitHub identifier of the received event.
        type: Type of the received event, such as "PushEvent" or
            "PullRequestEvent".
        actor_id: Unique identifier of the actor who triggered the event.
        actor_login: GitHub login/username of the actor who triggered
            the event.
        actor_url: API URL of the actor's GitHub user resource.
        repo_id: Unique identifier of the repository associated with
            the event.
        repo_name: Full name of the repository associated with the event,
            in owner/name format.
        repo_url: API URL of the repository associated with the event.
        created_at: Timestamp when the event was created.
    """
    id: str
    type: str

    actor_id: int
    actor_login: str
    actor_url: str

    repo_id: int
    repo_name: str
    repo_url: str

    created_at: str