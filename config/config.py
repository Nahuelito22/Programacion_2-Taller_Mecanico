import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secreto-default")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
