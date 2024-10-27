"""test adding motion

Revision ID: 2139b49ace1d
Revises: e38f8c59afcb
Create Date: 2024-10-27 21:46:52.744809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2139b49ace1d'
down_revision: Union[str, None] = 'e38f8c59afcb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
