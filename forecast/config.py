import os
from pathlib import Path


class Config(object):
    DEBUG = False
    TESTING = False
    FLASK_ENVIRONMENT = "development"

    PROJECT_ROOT = Path(__file__).absolute().parent.parent
    SWAGGER = {"title": "calapi"}


class ProductionConfig(Config):
    FLASK_ENVIRONMENT = "production"
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "calabi.be")


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENVIRONMENT = "development"
    CORS_ORIGINS = os.getenv(
        "CORS_ORIGINS", ["localhost", "http://localhost:4200", "http://localhost:3001"]
    )


class TestingConfig(Config):
    FLASK_ENVIRONMENT = "testing"
    TESTING = True
    CORS_ORIGINS = "localhost"
