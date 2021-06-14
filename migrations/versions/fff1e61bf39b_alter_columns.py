"""Alter columns

Revision ID: fff1e61bf39b
Revises: 019b04bea7ee
Create Date: 2021-06-15 00:53:43.076165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fff1e61bf39b'
down_revision = '019b04bea7ee'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "blogs",
        sa.Column('image', sa.String)
    )
    op.drop_column('users', 'image')


def downgrade():
    pass
