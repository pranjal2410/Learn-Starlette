"""Create users table

Revision ID: 29631e88080c
Revises: 
Create Date: 2021-06-13 19:58:32.972862

"""
import sqlalchemy
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
        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
        sqlalchemy.Column('username', sqlalchemy.String, unique=True),
        sqlalchemy.Column('password', sqlalchemy.String),
        sqlalchemy.Column('email', sqlalchemy.String, unique=True),
        sqlalchemy.Column('age', sqlalchemy.Integer),
        sqlalchemy.Column('is_admin', sqlalchemy.Boolean, default=False)
    )


def downgrade():
    op.drop_table('users')
