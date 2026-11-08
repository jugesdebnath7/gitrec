# src/gitrec/persistence/postgres/writer/user_writer.py


from __future__ import annotations

from typing import Any

from sqlalchemy.engine import Connection

from src.gitrec.persistence.postgres.writer.base_writer import BaseWriter


Record = dict[str, Any]
Records = dict[str, list[Record]]


class UserWriter(BaseWriter):
    """Persist user-related records to PostgreSQL."""

    def __init__(self, connection: Connection) -> None:
        super().__init__(
            connection=connection,
            schema="staging_user",
        )

    def write(self, records: Records) -> None:
        """Persist all user resources."""

        self._write_users(records["users"])
        self._write_profiles(records["profiles"])
        self._write_events(records["events"])
        self._write_followers(records["followers"])
        self._write_following(records["following"])
        self._write_gists(records["gists"])
        self._write_organizations(records["organizations"])
        self._write_received_events(records["received_events"])
        self._write_starred(records["starred"])
        self._write_repositories(records["user_repositories"])

    def _write_users(self, records: list[Record]) -> None:
        self._insert("user", records)

    def _write_profiles(self, records: list[Record]) -> None:
        self._insert("profile", records)

    def _write_events(self, records: list[Record]) -> None:
        self._insert("event", records)

    def _write_followers(self, records: list[Record]) -> None:
        self._insert("follower", records)

    def _write_following(self, records: list[Record]) -> None:
        self._insert("following", records)

    def _write_gists(self, records: list[Record]) -> None:
        self._insert("gist", records)

    def _write_organizations(self, records: list[Record]) -> None:
        self._insert("organization", records)

    def _write_received_events(self, records: list[Record]) -> None:
        self._insert("received_event", records)

    def _write_starred(self, records: list[Record]) -> None:
        self._insert("starred", records)

    def _write_repositories(self, records: list[Record]) -> None:
        self._insert("repository", records)
