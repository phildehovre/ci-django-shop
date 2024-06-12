from .base import *

DEBUG = False

ALLOWED_HOSTS = ['django-shop.up.railway.app', '127.0.0.1', 'localhost']

print('PRODUCTION')
STATIC_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/'

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
    },

    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}