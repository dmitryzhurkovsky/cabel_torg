"""Add a discount for an order

Revision ID: a45a98574a73
Revises: c91a4888a53d
Create Date: 2023-02-19 08:23:38.502853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45a98574a73'
down_revision = 'c91a4888a53d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('discount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'discount')
    # ### end Alembic commands ###
