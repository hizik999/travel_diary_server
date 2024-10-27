"""2 test adding motion

Revision ID: c7fe1318f505
Revises: 2139b49ace1d
Create Date: 2024-10-27 21:48:11.452900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7fe1318f505'
down_revision: Union[str, None] = '2139b49ace1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
