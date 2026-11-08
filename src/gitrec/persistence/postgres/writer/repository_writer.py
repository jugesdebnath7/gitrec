# src/gitrec/persistence/postgres/writer/repository_writer.py


from __future__ import annotations

from typing import Any

from sqlalchemy.engine import Connection

from src.gitrec.persistence.postgres.writer.base_writer import BaseWriter


Record = dict[str, Any]
Records = dict[str, list[Record]]


class RepositoryWriter(BaseWriter):
    """Persist repository-related records to PostgreSQL."""

    def __init__(self, connection: Connection) -> None:
        super().__init__(
            connection=connection,
            schema="staging_repository",
        )

    def write(self, records: Records) -> None:
        """Persist all repository resources."""

        self._write_repositories(records["repositories"])
        self._write_branches(records["branches"])
        self._write_commits(records["commits"])
        self._write_contributors(records["contributors"])
        self._write_forks(records["forks"])
        self._write_issues(records["issues"])
        self._write_languages(records["languages"])
        self._write_pull_requests(records["pull_requests"])
        self._write_readme(records["readme"])
        self._write_releases(records["releases"])
        self._write_tags(records["tags"])
        self._write_topics(records["topics"])

    def _write_repositories(self, records: list[Record]) -> None:
        self._insert("repository", records)

    def _write_branches(self, records: list[Record]) -> None:
        self._insert("branch", records)

    def _write_commits(self, records: list[Record]) -> None:
        self._insert("commit", records)

    def _write_contributors(self, records: list[Record]) -> None:
        self._insert("contributor", records)

    def _write_forks(self, records: list[Record]) -> None:
        self._insert("fork", records)

    def _write_issues(self, records: list[Record]) -> None:
        self._insert("issue", records)

    def _write_languages(self, records: list[Record]) -> None:
        self._insert("language", records)

    def _write_pull_requests(self, records: list[Record]) -> None:
        self._insert("pull_request", records)

    def _write_readme(self, records: list[Record]) -> None:
        self._insert("readme", records)

    def _write_releases(self, records: list[Record]) -> None:
        self._insert("release", records)

    def _write_tags(self, records: list[Record]) -> None:
        self._insert("tag", records)

    def _write_topics(self, records: list[Record]) -> None:
        self._insert("topic", records)
