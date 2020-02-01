from .base import *

import json

DEBUG = True
ALLOWED_HOSTS = '*'

ENV_CONFIG_FILE = os.path.join(BASE_DIR, 'settings/env_development.json')
ENV_CONFIG = json.loads(open(ENV_CONFIG_FILE).read())
print('loading: env_development.json')

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ENV_CONFIG['database']['name'],
        'USER': ENV_CONFIG['database']['user'],
        'PASSWORD': ENV_CONFIG['database']['password'],
        'HOST': ENV_CONFIG['database']['host'],
        'PORT': ENV_CONFIG['database']['port'],
        'CONN_MAX_AGE': 600,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    },
}