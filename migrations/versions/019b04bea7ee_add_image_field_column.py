"""Add image field column

Revision ID: 019b04bea7ee
Revises: 85746b511f15
Create Date: 2021-06-15 00:44:34.518746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019b04bea7ee'
down_revision = '85746b511f15'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'blogs',
        sa.Column('image', sa.String)
    )


def downgrade():
    op.drop_table('users')
