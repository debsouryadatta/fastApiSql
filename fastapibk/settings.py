from starlette.config import Config
from starlette.datastructures import Secret
# starlette comes with fastapi installation, its used for the database connection

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()
    
DATABASE_URL = config("DATABASE_URL", cast=Secret) 