"""5 test adding motion

Revision ID: 4b466b2d03b7
Revises: b31d36271a50
Create Date: 2024-10-27 22:07:13.769087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b466b2d03b7'
down_revision: Union[str, None] = 'b31d36271a50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
