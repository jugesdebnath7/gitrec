from __future__ import annotations

from alembic import context
from sqlalchemy import engine_from_config, pool

from src.gitrec.config.settings import get_settings
from src.gitrec.persistence.postgres.connection import PostgresConnection


config = context.config
settings = get_settings()

# Use the existing application's database configuration.
config.set_main_option(
    "sqlalchemy.url", 
    settings.postgres.dsn.replace("%", "%%"),
)

# Replace with your SQLAlchemy/SQLModel metadata if needed in the future.
target_metadata = None  

def run_migrations_offline() -> None:
    """Run migrations without creating a database connection (offline mode)."""
    context.configure(
        url=settings.postgres.dsn,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations using the application's connection manager (online mode)."""
    with PostgresConnection(settings=settings) as postgres:
        with postgres.engine.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
                compare_type=True,  # Enable type comparison for migrations
            )

            with context.begin_transaction():
                context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()