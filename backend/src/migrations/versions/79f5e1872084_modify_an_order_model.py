"""Modify an order model

Revision ID: 79f5e1872084
Revises: 11ca0ba53c0d
Create Date: 2023-01-23 07:42:13.098569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79f5e1872084'
down_revision = '11ca0ba53c0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('images', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_articles_id'), 'articles', ['id'], unique=False)
    op.create_table('delivery_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payload', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_delivery_types_id'), 'delivery_types', ['id'], unique=False)
    op.create_table('partners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_partners_id'), 'partners', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('promo_code', sa.String(length=50), nullable=True),
    sa.Column('company_name', sa.String(length=50), nullable=True),
    sa.Column('unp', sa.String(length=9), nullable=True),
    sa.Column('legal_address', sa.String(length=128), nullable=True),
    sa.Column('IBAN', sa.String(length=34), nullable=True),
    sa.Column('BIC', sa.String(length=50), nullable=True),
    sa.Column('serving_bank', sa.String(length=128), nullable=True),
    sa.Column('full_name', sa.String(length=50), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('house', sa.String(length=12), nullable=True),
    sa.Column('flat', sa.String(length=12), nullable=True),
    sa.Column('delivery_type_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['delivery_type_id'], ['delivery_types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    op.create_table('product_orders',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.CheckConstraint('amount > 0', name='check_count_should_be_positive'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_orders')
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_partners_id'), table_name='partners')
    op.drop_table('partners')
    op.drop_index(op.f('ix_delivery_types_id'), table_name='delivery_types')
    op.drop_table('delivery_types')
    op.drop_index(op.f('ix_articles_id'), table_name='articles')
    op.drop_table('articles')
    # ### end Alembic commands ###