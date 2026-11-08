# src/gitrec/persistence/postgres/writer/base_writer.py

from __future__ import annotations

from typing import Any

from sqlalchemy import MetaData, Table, insert
from sqlalchemy.engine import Connection


Record = dict[str, Any]


class BaseWriter:
    """Provide common PostgreSQL persistence operations."""

    def __init__(
        self,
        connection: Connection,
        schema: str,
    ) -> None:
        self._connection = connection
        self._schema = schema
        self._metadata = MetaData()
        self._tables: dict[str, Table] = {}

    def _get_table(self, table_name: str) -> Table:
        """Reflect and cache a PostgreSQL staging table."""

        if table_name not in self._tables:
            self._tables[table_name] = Table(
                table_name,
                self._metadata,
                schema=self._schema,
                autoload_with=self._connection,
            )

        return self._tables[table_name]

    def _insert(
        self,
        table_name: str,
        records: list[Record],
    ) -> None:
        """Bulk insert records into a staging table."""

        if not records:
            return

        table = self._get_table(table_name)

        rows = []

        for index, record in enumerate(records):
            unknown_columns = (
                set(record) - set(table.columns.keys())
            )

            if unknown_columns:
                raise ValueError(
                    f"Unknown columns for "
                    f"{table.fullname}, record {index}: "
                    f"{sorted(unknown_columns)}"
                )

            rows.append(record)

        self._connection.execute(
            insert(table),
            rows,
        )
