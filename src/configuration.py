from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()


@dataclass
class DatabaseConfig:
    host: str = getenv('DB_HOST')
    port: str = getenv('DB_PORT')
    name: str = getenv('DB_NAME')
    MONGODB_URL = f'mongodb://{host}:{port}'
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[name]
    collection = db['payments']


@dataclass
class BotConfig:
    token: str = getenv('BOT_TOKEN')


@dataclass
class Configuration:
    debug = bool(getenv('DEBUG'))
    db = DatabaseConfig()
    bot = BotConfig()


conf = Configuration()
