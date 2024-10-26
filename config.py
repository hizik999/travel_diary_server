from enum import Enum


class Config(Enum):
    # HOST = "localhost"
    # PORT = 8080
    # DEBUG = False
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/travel_diary"