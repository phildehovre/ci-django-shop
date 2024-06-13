from .base import *

DEBUG = True

ALLOWED_HOSTS = ['django-shop.up.railway.app','127.0.0.1', 'localhost']
print('DEVELOPMENT')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if config("DJANGO_ENVIRONMENT")  == "production":
    STATIC_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/django_shop'

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
        },

        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        },
    }
else :
    STATIC_URL= '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage"
        },

        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }