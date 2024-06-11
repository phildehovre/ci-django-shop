from .base import *

DEBUG = False

ALLOWED_HOSTS = ['django-shop.up.railway.app']

STATIC_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/static/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
    },

    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}