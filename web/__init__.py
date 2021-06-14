from starlette.config import Config
import databases
import sqlalchemy
import os
from starlette_jwt import JWTAuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

config = Config(os.path.join(os.getcwd(), '.env'))
database = databases.Database(config('DATABASE_URL'))

metadata = sqlalchemy.MetaData()


async def startup():
    print('Application has started')


middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*']),
    Middleware(AuthenticationMiddleware,
               backend=JWTAuthenticationBackend(
                       secret_key=config('SECRET_KEY'),
                       prefix='Bearer',
                       algorithm='HS256',
    )),
    Middleware(SessionMiddleware, secret_key=config('SECRET_KEY'))
]
