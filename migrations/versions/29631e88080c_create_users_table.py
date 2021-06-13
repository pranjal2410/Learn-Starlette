"""Create users table

Revision ID: 29631e88080c
Revises: 
Create Date: 2021-06-13 19:58:32.972862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29631e88080c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String, unique=True),
        sa.Column('password', sa.String),
        sa.Column('email', sa.String, unique=True),
        sa.Column('age', sa.Integer),
        sa.Column('is_admin', sa.Boolean, default=False)
    )


def downgrade():
    op.drop_table('users')
