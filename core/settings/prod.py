import os

from .base import *


DEBUG = False

ALLOWED_HOSTS = ["*"]

ENVIRONMENT = 'producao'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME', ''),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),
        'PORT': 5432,
    }
}

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = os.getenv('REDIS_DB', '')
REDIS_CACHE_DB = os.getenv('REDIS_CACHE_DB', '')
RQ_QUEUES = {
    'default': {
        'HOST': REDIS_HOST,
        'PORT': REDIS_PORT,
        'DB': REDIS_DB,
        'DEFAULT_TIMEOUT': 360,
    },
}

INTERVALO_ATUALIZACAO_NOTEBOOKS = 7200
