import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    BASE_URL = os.getenv('BASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

