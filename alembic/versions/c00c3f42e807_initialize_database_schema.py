"""initialize database schema

Revision ID: c00c3f42e807
Revises: 
Create Date: 2026-10-22 17:18:06.922318

"""
from typing import Sequence, Union
from pathlib import Path

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c00c3f42e807'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the initial database schema."""
    schema_file = (
        Path(__file__).resolve().parents[2] 
        / "src"
        / "gitrec"
        / "persistence"
        / "postgres"
        / "sql"
        / "schema.sql"
    )

    schema_sql = schema_file.read_text(encoding="utf-8")

    # The underlying pyscopg2 cursor to execute the full PostgreSQL script, 
    # including comments and semicolons.
    connection = op.get_bind()
    dbapi_connection = connection.connection.driver_connection

    with dbapi_connection.cursor() as cursor:
        cursor.execute(schema_sql)


def downgrade() -> None:
    """Define the reverse schema operation before downgrade."""
    raise NotImplementedError(
        "Downgrade is not implemented for this migration."
    )
