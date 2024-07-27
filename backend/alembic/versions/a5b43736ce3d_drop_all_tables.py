"""drop all tables

Revision ID: a5b43736ce3d
Revises: 90614c882db4
Create Date: 2024-07-27 14:50:47.791212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5b43736ce3d'
down_revision: Union[str, None] = '90614c882db4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.drop_table('foods')
    # op.drop_table('users')
    # op.drop_table('storages')
    # op.drop_table('recipes')
    # op.drop_table('recipe_foods')
    op.execute('DROP TABLE IF EXISTS recipe_foods CASCADE')
    op.execute('DROP TABLE IF EXISTS foods CASCADE')
    op.execute('DROP TABLE IF EXISTS recipes CASCADE')
    op.execute('DROP TABLE IF EXISTS users CASCADE')
    op.execute('DROP TABLE IF EXISTS fridges CASCADE')


def downgrade() -> None:
    pass
