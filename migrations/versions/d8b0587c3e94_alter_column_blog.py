"""Alter column blog

Revision ID: d8b0587c3e94
Revises: fff1e61bf39b
Create Date: 2021-06-15 01:32:43.261105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8b0587c3e94'
down_revision = 'fff1e61bf39b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "blogs",
        sa.Column("title", sa.String)
    )


def downgrade():
    pass
