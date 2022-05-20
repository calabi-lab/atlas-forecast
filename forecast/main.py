import os

from forecast.factory import create_app
from forecast import config

flask_env = os.getenv("FLASK_ENV", "development")
config_object: config.Config

if flask_env == "production":
    config_object = config.ProductionConfig()
elif flask_env == "development":
    config_object = config.DevelopmentConfig()
else:
    config_object = config.TestingConfig()

app = create_app(name=__name__, config_object=config_object)
