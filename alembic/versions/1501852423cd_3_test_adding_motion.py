"""3 test adding motion

Revision ID: 1501852423cd
Revises: c7fe1318f505
Create Date: 2024-10-27 22:02:19.388985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1501852423cd'
down_revision: Union[str, None] = 'c7fe1318f505'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
