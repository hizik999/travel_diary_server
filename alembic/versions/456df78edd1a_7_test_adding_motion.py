"""7 test adding motion

Revision ID: 456df78edd1a
Revises: b3f673591048
Create Date: 2024-10-27 22:29:04.621844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '456df78edd1a'
down_revision: Union[str, None] = 'b3f673591048'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
