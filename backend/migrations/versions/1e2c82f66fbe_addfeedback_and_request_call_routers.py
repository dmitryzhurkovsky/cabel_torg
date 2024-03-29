"""addfeedback and request_call routers

Revision ID: 1e2c82f66fbe
Revises: 78927e043df4
Create Date: 2023-02-26 13:14:40.526538

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1e2c82f66fbe'
down_revision = '78927e043df4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service__feedback',
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service__feedback_id'), 'service__feedback', ['id'], unique=False)
    op.create_table('service__request_call',
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('type', postgresql.ENUM('U', 'GR', name='request_call_status'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service__request_call_id'), 'service__request_call', ['id'], unique=False)
    op.create_table('service__vendor_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('director_fullname', sa.String(length=255), nullable=True),
    sa.Column('unp', sa.String(length=9), nullable=True),
    sa.Column('OKPO', sa.String(length=10), nullable=True),
    sa.Column('legal_address', sa.String(length=256), nullable=True),
    sa.Column('postal_address', sa.String(length=256), nullable=True),
    sa.Column('phone_and_fax', sa.String(length=128), nullable=True),
    sa.Column('serving_bank', sa.String(length=128), nullable=True),
    sa.Column('serving_bank_short', sa.String(length=128), nullable=True),
    sa.Column('IBAN', sa.String(length=35), nullable=True),
    sa.Column('RUR', sa.String(length=35), nullable=True),
    sa.Column('instagram_url', sa.String(), nullable=True),
    sa.Column('facebook_url', sa.String(), nullable=True),
    sa.Column('vk_url', sa.String(), nullable=True),
    sa.Column('telegram_url', sa.String(), nullable=True),
    sa.Column('twitter_url', sa.String(), nullable=True),
    sa.Column('tiktok_url', sa.String(), nullable=True),
    sa.Column('youtube_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service__vendor_info_id'), 'service__vendor_info', ['id'], unique=False)
    op.create_table('service__addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('payload', sa.String(), nullable=True),
    sa.Column('vendor_info_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['vendor_info_id'], ['service__vendor_info.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service__addresses_id'), 'service__addresses', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_service__addresses_id'), table_name='service__addresses')
    op.drop_table('service__addresses')
    op.drop_index(op.f('ix_service__vendor_info_id'), table_name='service__vendor_info')
    op.drop_table('service__vendor_info')
    op.drop_index(op.f('ix_service__request_call_id'), table_name='service__request_call')
    op.drop_table('service__request_call')
    op.drop_index(op.f('ix_service__feedback_id'), table_name='service__feedback')
    op.drop_table('service__feedback')
    # ### end Alembic commands ###
