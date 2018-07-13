import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "itsasecret"
    GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID")
    GITHUB_SECRET_ID = os.environ.get("GITHUB_SECRET_ID")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR.strip("\\config"), "db/dev.db")

class TestingConfig(BaseConfig):
    DEBUG = True
    ENV = 'testing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db/test.db")

class ProductionConfig(BaseConfig):
    ENV = 'production'
