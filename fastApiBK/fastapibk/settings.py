from starlette.config import Config
from starlette.datastructures import Secret
from datetime import timedelta
# starlette comes with fastapi installation, its used for the database connection

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()
    
DATABASE_URL = config("DATABASE_URL", cast=Secret)
JWT_SECRET_KEY = config("JWT_SECRET_KEY", cast=Secret)
JWT_ALGORITHYM = config("JWT_ALGORITHYM")
# JWT_EXPIRY_TIME = config("JWT_EXPIRY_TIME", cast=timedelta) # in minutes