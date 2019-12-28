import os

FITCLIB_ENV = os.environ.get('FITCLIB_ENV', 'production')
if FITCLIB_ENV == 'development':
    from .development import *
else:
    from .production import *
