# scripts/check_tables.py

from sqlalchemy import text

from src.gitrec.config.settings import get_settings
from src.gitrec.persistence.postgres.connection import PostgresConnection


def check_tables() -> None:
    with PostgresConnection(get_settings()) as postgres:
        with postgres.engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT table_schema, table_name
                    FROM information_schema.tables
                    WHERE table_type = 'BASE TABLE'
                      AND table_schema NOT IN (
                          'pg_catalog',
                          'information_schema'
                      )
                    ORDER BY table_schema, table_name
                """)
            )

            tables = result.fetchall()

            if not tables:
                print("No application tables found.")
                return

            print("Tables found in PostgreSQL:")
            for schema, table in tables:
                print(f"  {schema}.{table}")

def check_schemas() -> None:
    with PostgresConnection(get_settings()) as postgres:
        with postgres.engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT schema_name
                    FROM information_schema.schemata
                    WHERE schema_name IN (
                        'staging_repository',
                        'staging_user',
                        'production_repository',
                        'production_user'
                    )
                    ORDER BY schema_name
                """)
            )

            schemas = result.fetchall()

            if not schemas:
                print("No application schemas found.")
                return

            print("Schemas found in PostgreSQL:")
            for (schema,) in schemas:
                print(f"  {schema}")

if __name__ == "__main__":
    check_tables()
    check_schemas()
                    