from django.conf import settings
import yaml

settings.APP_NAME = getattr(settings, 'APP_NAME', "default_value")
settings.APP_VERSION = getattr(settings, 'APP_VERSION', "1.0")
settings.APP_URL = getattr(settings, 'APP_URL', "https://example.com/")
settings.FRONT_URL = getattr(settings, 'FRONT_URL', "http://localhost:5173/")

def load_config(filename='config.yml'):
        with open(filename, 'r') as file:
            config = yaml.safe_load(file)
        return config

settings.CONFIG = getattr(settings, 'CONFIG', load_config())