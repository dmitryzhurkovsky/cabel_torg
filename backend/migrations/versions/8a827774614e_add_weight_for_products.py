"""add weight for products

Revision ID: 8a827774614e
Revises: c335a69dcd44
Create Date: 2023-03-19 20:33:30.029651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a827774614e'
down_revision = 'c335a69dcd44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('weight', sa.DECIMAL(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'weight')
    # ### end Alembic commands ###
