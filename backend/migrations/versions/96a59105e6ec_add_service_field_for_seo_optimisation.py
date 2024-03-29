"""Add service field for SEO-optimisation

Revision ID: 96a59105e6ec
Revises: 6bc08dd9566b
Create Date: 2023-04-18 08:07:43.411710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96a59105e6ec'
down_revision = '6bc08dd9566b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('site_link', sa.String(), nullable=True))
    op.add_column('categories', sa.Column('site_page_title', sa.String(), nullable=True))
    op.add_column('categories', sa.Column('site_page_description', sa.String(), nullable=True))
    op.add_column('products', sa.Column('site_link', sa.String(), nullable=True))
    op.add_column('products', sa.Column('site_page_title', sa.String(), nullable=True))
    op.add_column('products', sa.Column('site_page_description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'site_page_description')
    op.drop_column('products', 'site_page_title')
    op.drop_column('products', 'site_link')
    op.drop_column('categories', 'site_page_description')
    op.drop_column('categories', 'site_page_title')
    op.drop_column('categories', 'site_link')
    # ### end Alembic commands ###
