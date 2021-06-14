"""Alter column blog

Revision ID: b80caede2ace
Revises: d8b0587c3e94
Create Date: 2021-06-15 01:33:47.490859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80caede2ace'
down_revision = 'd8b0587c3e94'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column(
        "blogs",
        "title"
    )
    op.add_column(
        "blogs",
        sa.Column("title", sa.String, unique=True)
    )


def downgrade():
    pass
