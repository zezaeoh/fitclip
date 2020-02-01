import os

FITCLIP_ENV = os.environ.get('FITCLIP_ENV', 'production')
if FITCLIP_ENV == 'development':
    from .development import *
else:
    from .production import *
