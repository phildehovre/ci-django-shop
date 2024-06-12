from .base import *

DEBUG = True

ALLOWED_HOSTS = ['django-shop.up.railway.app','127.0.0.1', 'localhost']


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Use local storage for static files

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
    },

     "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}