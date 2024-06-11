from .base import *

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[])

STATIC_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/static/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
    },

    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}