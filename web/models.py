import sqlalchemy
from web import metadata

users = sqlalchemy.Table(
    'users',
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('username', sqlalchemy.String, unique=True),
    sqlalchemy.Column('password', sqlalchemy.String),
    sqlalchemy.Column('email', sqlalchemy.String, unique=True),
    sqlalchemy.Column('age', sqlalchemy.Integer),
    sqlalchemy.Column('is_admin', sqlalchemy.Boolean, default=False)
)
