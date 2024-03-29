"""Add some fields for banner

Revision ID: eee8ae7304f3
Revises: 9470a62da656
Create Date: 2023-03-25 16:30:14.869500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eee8ae7304f3'
down_revision = '9470a62da656'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service__banners', sa.Column('button_name', sa.String(), nullable=True))
    op.add_column('service__banners', sa.Column('button_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service__banners', 'button_link')
    op.drop_column('service__banners', 'button_name')
    # ### end Alembic commands ###
