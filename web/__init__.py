from starlette.config import Config
import databases
import sqlalchemy
import os

config = Config(os.path.join(os.getcwd(), '.env'))
database = databases.Database(config('DATABASE_URL'))

metadata = sqlalchemy.MetaData()
