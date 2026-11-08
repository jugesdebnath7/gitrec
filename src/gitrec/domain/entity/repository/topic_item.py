# src/gitrec/domain/entity/repository/topic_item.py

from __future__ import annotations

from pydantic import BaseModel


class TopicItem(BaseModel):
    """
    Represents a topic associated with a repository within the GitRec domain.

    The entity contains the repository association and topic name used by
    downstream storage and feature-engineering pipelines.

    Attributes:
        repo_id: Unique identifier of the repository that has the topic.
        topic: Name of the topic associated with the repository.
    """
    repo_id: int
    topic: str
