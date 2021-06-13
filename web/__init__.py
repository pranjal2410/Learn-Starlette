from starlette.config import Config
import databases
import os

config = Config(os.path.join(os.getcwd(), '.env'))
database = databases.Database(config('DATABASE_URL'))
