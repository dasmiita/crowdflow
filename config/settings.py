import os
import dj_database_url

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

ALLOWED_HOSTS = ['*']

DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL)

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-_5n38_)h3$-g33+#2yr@bc9t3h)kh3%e0x3m09nsproi#)in77')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'