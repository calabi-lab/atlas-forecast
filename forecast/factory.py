from flask import Flask
from calapi import config
from flasgger import Swagger
from loguru import logger
from dotenv import load_dotenv

load_dotenv()


def create_app(
    name: str = __name__, config_object: config.Config = config.DevelopmentConfig()
):
    app = Flask(name)

    app.config.from_object(config_object)

    Swagger(app)

    logger.info("🏇 Starting up app")

    return app
