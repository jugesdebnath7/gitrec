# src/gitrec/domain/mapper/repository/topic_item.py

from __future__ import annotations

from typing import Any

from src.gitrec.domain.entity.repository.topic_item import TopicItem


class TopicMapper:
    """
    Maps GitHub repository topic responses into domain topic entities.
    """

    @staticmethod
    def to_topic_item(
        data: dict[str, Any],
        repo_id: int,
    ) -> list[TopicItem]:
        """
        Convert GitHub repository topics into TopicItem entities.

        Args:
            data: Raw repository data containing the topics returned by
                the GitHub API.
            repo_id: Unique identifier of the repository associated with
                the topics.

        Returns:
            A list of TopicItem instances representing the repository topics.
        """
        topics = data.get("names", [])

        return [
            TopicItem(
                repo_id=repo_id,
                topic=topic,
            )
            for topic in topics
        ]