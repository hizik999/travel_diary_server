"""v1_5 added user_imei

Revision ID: e8265d176d23
Revises: 461409078b3d
Create Date: 2024-11-04 20:43:46.261388

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8265d176d23'
down_revision: Union[str, None] = '461409078b3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('motions', sa.Column('user_imei', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('motions', 'user_imei')
    # ### end Alembic commands ###