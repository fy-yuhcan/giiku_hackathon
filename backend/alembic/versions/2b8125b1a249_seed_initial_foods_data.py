"""seed initial foods data

Revision ID: 2b8125b1a249
Revises: 313dbaa66f20
Create Date: 2024-07-27 15:48:38.594114

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import os
import csv


# revision identifiers, used by Alembic.
revision: str = '2b8125b1a249'
down_revision: Union[str, None] = '313dbaa66f20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, '../../data/seed_foods_data.csv')

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            op.execute(
                sa.text(
                    "INSERT INTO foods (name, unit) VALUES (:name, :unit)"
                ).bindparams(name=row['name'], unit=row['unit'])
            )


def downgrade() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, '../../data/seed_foods_data.csv')

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            op.execute(
                sa.text(
                    "DELETE FROM foods WHERE name = :name AND unit = :unit"
                ),
                name=row['name'],
                unit=row['unit']
            )