import sqlalchemy
from sqlalchemy.orm import relationship

from web import metadata
import datetime


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('username', sqlalchemy.String, unique=True),
    sqlalchemy.Column('password', sqlalchemy.String),
    sqlalchemy.Column('email', sqlalchemy.String, unique=True),
    sqlalchemy.Column('age', sqlalchemy.Integer),
    sqlalchemy.Column('is_admin', sqlalchemy.Boolean, default=False),
)

blogs = sqlalchemy.Table(
    'blogs',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('title', sqlalchemy.String, unique=True),
    sqlalchemy.Column('text', sqlalchemy.Text),
    sqlalchemy.Column('created', sqlalchemy.DateTime, default=datetime.datetime.now()),
    sqlalchemy.Column('image', sqlalchemy.String),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
)
