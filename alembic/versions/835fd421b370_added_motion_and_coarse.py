"""added motion and coarse

Revision ID: 835fd421b370
Revises: 6c9376c46a07
Create Date: 2024-10-28 11:53:21.550233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '835fd421b370'
down_revision: Union[str, None] = '6c9376c46a07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_name', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###
