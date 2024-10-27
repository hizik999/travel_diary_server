"""4 test adding motion

Revision ID: b31d36271a50
Revises: 1501852423cd
Create Date: 2024-10-27 22:05:15.640583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b31d36271a50'
down_revision: Union[str, None] = '1501852423cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
