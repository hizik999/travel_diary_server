"""6 test adding motion

Revision ID: b3f673591048
Revises: 4b466b2d03b7
Create Date: 2024-10-27 22:11:23.930789

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3f673591048'
down_revision: Union[str, None] = '4b466b2d03b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
