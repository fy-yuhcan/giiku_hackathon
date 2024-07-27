"""seed test user

Revision ID: 901ad71c201c
Revises: 2b8125b1a249
Create Date: 2024-07-27 19:18:25.426856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '901ad71c201c'
down_revision: Union[str, None] = '2b8125b1a249'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.text(
            "INSERT INTO users (name, password) VALUES (:name, :password)"
        ).bindparams(
            name='test',
            password='$2b$12$RjltKaFydZvQU/eByhSnI.NuPmutfbqGhvaUyYAHHQNnLtXQBhBpm'
        )
    )


def downgrade() -> None:
    op.execute(
        sa.text(
            "DELETE FROM users WHERE name = :name AND password = :password"
        ).bindparams(
            name='test',
            password='$2b$12$RjltKaFydZvQU/eByhSnI.NuPmutfbqGhvaUyYAHHQNnLtXQBhBpm'
        )
    )