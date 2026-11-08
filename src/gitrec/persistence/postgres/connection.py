# src/gitrec/persistence/postgres/connection.py

from __future__ import annotations

import logging
from types import TracebackType
from typing import Self

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from src.gitrec.config.settings import Settings


logger = logging.getLogger(__name__)


class PostgresConnection:
    """Manage PostgreSQL connectivity using a SQLAlchemy engine."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._engine: Engine | None = None

    @property
    def engine(self) -> Engine:
        """Return the initialized SQLAlchemy engine."""
        if self._engine is None:
            raise RuntimeError(
                "PostgreSQL engine is not initialized. "
                "Call connect() first."
            )

        return self._engine

    def connect(self) -> Self:
        """Create the engine and verify database connectivity."""
        if self._engine is not None:
            return self

        engine = create_engine(
            self._settings.postgres.dsn,
            pool_pre_ping=True,
            pool_size=self._settings.postgres.pool_size,
            max_overflow=self._settings.postgres.max_overflow,
            pool_timeout=self._settings.postgres.pool_timeout,
            pool_recycle=self._settings.postgres.pool_recycle,
            echo=self._settings.log_level.upper() == "DEBUG",
        )

        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))

        except Exception:
            engine.dispose()
            logger.exception(
                "Failed to initialize PostgreSQL connectivity."
            )
            raise

        self._engine = engine

        logger.info("PostgreSQL connection established.")
        return self

    def health_check(self) -> bool:
        """Return whether PostgreSQL is reachable."""
        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))

            return True

        except SQLAlchemyError:
            logger.exception("PostgreSQL health check failed.")
            return False

    def close(self) -> None:
        """Dispose of the connection pool and release resources."""
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None

            logger.info("PostgreSQL connection pool closed.")

    def __enter__(self) -> Self:
        """Initialize connectivity when entering a context."""
        return self.connect()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Release resources when leaving a context."""
        self.close()
