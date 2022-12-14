"""empty message

Revision ID: 10585ee4d545
Revises: 30918e0d4378
Create Date: 2022-09-15 18:08:26.465436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10585ee4d545'
down_revision = '30918e0d4378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
