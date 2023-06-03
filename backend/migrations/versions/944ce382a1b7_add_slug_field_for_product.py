"""Add slug field for product

Revision ID: 944ce382a1b7
Revises: 8d74b94e8fdd
Create Date: 2023-05-28 13:28:50.250110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '944ce382a1b7'
down_revision = '8d74b94e8fdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('vendor_code_ru', sa.String(), nullable=True))
    op.alter_column('products', 'vendor_code',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'vendor_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('products', 'vendor_code_ru')
    # ### end Alembic commands ###