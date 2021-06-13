from starlette.config import Config
import databases
import sqlalchemy
import os
from starlette_jwt import JWTAuthenticationBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from sqlalchemy.orm import sessionmaker

config = Config(os.path.join(os.getcwd(), '.env'))
database = databases.Database(config('DATABASE_URL'))

metadata = sqlalchemy.MetaData()


async def startup():
    print('Application has started')


middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*']),
    Middleware(AuthenticationMiddleware,
               backend=JWTAuthenticationBackend(
                       secret_key='a9cb4ea36a5175e2cb840db5fa2210254d25c25d6344ebebd493af00bf922416',
                       prefix='Bearer'
    ))
]
