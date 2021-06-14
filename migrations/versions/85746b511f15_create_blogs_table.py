"""Create blogs table

Revision ID: 85746b511f15
Revises: 29631e88080c
Create Date: 2021-06-14 18:37:47.662661

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = '85746b511f15'
down_revision = '29631e88080c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'blogs',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('text', sa.Text),
        sa.Column('created', sa.DateTime, default=datetime.datetime.now()),
        sa.Column('user_id', sa.Integer, sa.ForeignKey("users.id"), nullable=False),
    )


def downgrade():
    op.drop_table('blogs')
