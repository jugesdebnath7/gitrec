
# src/gitrec/persistence/postgres/validation/schema_validator.py

from __future__ import annotations

import json
from datetime import date, datetime
from typing import Any

from sqlalchemy import (
    BigInteger,
    Boolean,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.engine import Engine
from sqlalchemy.sql.sqltypes import Text


Record = dict[str, Any]
Records = dict[str, list[Record]]


class SchemaValidationError(ValueError):
    """Raised when records do not satisfy the database schema."""


class SchemaValidator:
    """Validate database-ready records against PostgreSQL staging schemas."""

    SCHEMAS = {
        "repository": {
            "repositories": "repository",
            "branches": "branch",
            "commits": "commit",
            "contributors": "contributor",
            "forks": "fork",
            "issues": "issue",
            "languages": "language",
            "pull_requests": "pull_request",
            "readme": "readme",
            "releases": "release",
            "tags": "tag",
            "topics": "topic",
        },
        "user": {
            "users": "user",
            "profiles": "profile",
            "events": "event",
            "followers": "follower",
            "following": "following",
            "gists": "gist",
            "organizations": "organization",
            "received_events": "received_event",
            "starred": "starred",
            "user_repositories": "repository",
        },
    }

    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._metadata = MetaData()
        self._tables: dict[tuple[str, str], Table] = {}

    def validate(
        self,
        resource: str,
        records: Records,
    ) -> None:
        """Validate all records against their staging schema."""

        if resource not in self.SCHEMAS:
            raise ValueError(f"Unknown resource: {resource}")

        expected_resources = self.SCHEMAS[resource]

        unknown_resources = set(records) - set(expected_resources)

        if unknown_resources:
            raise SchemaValidationError(
                f"Unknown {resource} resources: "
                f"{sorted(unknown_resources)}"
            )

        for resource_name, table_name in expected_resources.items():
            resource_records = records.get(resource_name, [])

            self._validate_resource(
                schema=f"staging_{resource}",
                table_name=table_name,
                records=resource_records,
            )

    def validate_all(
        self,
        repository_records: Records,
        user_records: Records,
    ) -> None:
        """Validate repository and user records."""

        self.validate("repository", repository_records)
        self.validate("user", user_records)

    def _get_table(
        self,
        schema: str,
        table_name: str,
    ) -> Table:
        """Reflect and cache a PostgreSQL table."""

        key = (schema, table_name)

        if key not in self._tables:
            self._tables[key] = Table(
                table_name,
                self._metadata,
                schema=schema,
                autoload_with=self._engine,
            )

        return self._tables[key]

    def _validate_resource(
        self,
        schema: str,
        table_name: str,
        records: list[Record],
    ) -> None:
        """Validate records against a specific table."""

        if not isinstance(records, list):
            raise SchemaValidationError(
                f"{schema}.{table_name}: expected a list of records."
            )

        if not records:
            return

        table = self._get_table(schema, table_name)
        columns = set(table.columns.keys())

        for index, record in enumerate(records):
            location = f"{schema}.{table_name}, record {index}"

            if not isinstance(record, dict):
                raise SchemaValidationError(
                    f"{location}: expected a dictionary."
                )

            unknown_columns = set(record) - columns

            if unknown_columns:
                raise SchemaValidationError(
                    f"{location}: unknown columns "
                    f"{sorted(unknown_columns)}."
                )

            for column in table.columns:
                name = column.name

                if name not in record:
                    if (
                        not column.nullable
                        and column.server_default is None
                        and column.default is None
                    ):
                        raise SchemaValidationError(
                            f"{location}: missing required column '{name}'."
                        )
                    continue

                value = record[name]

                if value is None:
                    if not column.nullable:
                        raise SchemaValidationError(
                            f"{location}: column '{name}' "
                            "does not allow NULL."
                        )
                    continue

                self._validate_type(
                    value=value,
                    column=column,
                    location=location,
                )

    @staticmethod
    def _validate_type(
        value: Any,
        column: Any,
        location: str,
    ) -> None:
        """Validate Python values against SQLAlchemy column types."""

        column_type = column.type
        valid = True

        if isinstance(column_type, Boolean):
            valid = isinstance(value, bool)

        elif isinstance(column_type, BigInteger):
            valid = isinstance(value, int) and not isinstance(value, bool)

        elif isinstance(column_type, Integer):
            valid = isinstance(value, int) and not isinstance(value, bool)

        elif isinstance(column_type, DateTime):
            valid = isinstance(value, datetime)

        elif isinstance(column_type, String):
            valid = isinstance(value, str)

        elif isinstance(column_type, Text):
            valid = isinstance(value, str)

        elif isinstance(column_type, JSONB):
            try:
                json.dumps(value)
            except (TypeError, ValueError):
                valid = False

        if not valid:
            raise SchemaValidationError(
                f"{location}: invalid value for column "
                f"'{column.name}'. Expected {column_type}, "
                f"got {type(value).__name__}."
            )
