"""create new tables

Revision ID: 313dbaa66f20
Revises: a5b43736ce3d
Create Date: 2024-07-27 15:28:28.115113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '313dbaa66f20'
down_revision: Union[str, None] = 'a5b43736ce3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE foods (
        id SERIAL PRIMARY KEY,
        name VARCHAR NOT NULL,
        unit VARCHAR NOT NULL
    )
    """)
    op.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR NOT NULL,
        password VARCHAR NOT NULL
    )
    """)
    op.execute("""
    CREATE TABLE storages (
        id SERIAL PRIMARY KEY,
        food_id INTEGER NOT NULL REFERENCES foods(id),
        user_id INTEGER NOT NULL REFERENCES users(id),
        added_at TIMESTAMP NOT NULL,
        quantity FLOAT NOT NULL
    )
    """)
    op.execute("""
    CREATE TABLE recipes (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES users(id),
        title VARCHAR NOT NULL,
        content VARCHAR NOT NULL
    )
    """)
    op.execute("""
    CREATE TABLE recipe_foods (
        id SERIAL PRIMARY KEY,
        food_id INTEGER NOT NULL REFERENCES foods(id),
        recipe_id INTEGER NOT NULL REFERENCES recipes(id),
        quantity FLOAT NOT NULL
    )
    """)


def downgrade() -> None:
    pass
