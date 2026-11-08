# src/gitrec/persistence/service.py


from __future__ import annotations

from src.gitrec.domain.entity.repository.repository_item import RepositoryItem
from src.gitrec.domain.entity.user.user_item import UserItem
from src.gitrec.persistence.postgres.connection import PostgresConnection
from src.gitrec.persistence.postgres.mapper.repository import RepositoryMapper
from src.gitrec.persistence.postgres.mapper.user import UserMapper
from src.gitrec.persistence.postgres.validation.schema_validator import (
    SchemaValidator,
)
from src.gitrec.persistence.postgres.writer.repository_writer import RepositoryWriter
from src.gitrec.persistence.postgres.writer.user_writer import UserWriter


class PersistenceService:
    """Coordinate mapping, validation, and transactional persistence."""

    def __init__(
        self,
        connection: PostgresConnection,
    ) -> None:
        self._connection = connection

        self._repository_mapper = RepositoryMapper()
        self._user_mapper = UserMapper()
        self._schema_validator = SchemaValidator(connection.engine)

    def persist(
        self,
        repositories: list[RepositoryItem],
        users: list[UserItem],
    ) -> None:
        """Validate and persist repository and user aggregates."""

        # Step 1: Map domain entities.
        repository_records = self._repository_mapper.flatten(repositories)
        user_records = self._user_mapper.flatten(users)

        # Step 2: Validate against PostgreSQL staging schemas.
        self._schema_validator.validate_all(
            repository_records=repository_records,
            user_records=user_records,
        )

        # Step 3: Persist both resources in one transaction.
        with self._connection.engine.begin() as connection:
            RepositoryWriter(connection).write(repository_records)
            UserWriter(connection).write(user_records)
