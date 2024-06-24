from .base import *

ALLOWED_HOSTS = ['django-shop.up.railway.app','127.0.0.1', 'localhost']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print("ENVIRONMENT", config('DJANGO_ENVIRONMENT'))

if config("DJANGO_ENVIRONMENT")  == "production":
    STATIC_URL = f'{AWS_S3_URL_PROTOCOL}//{AWS_S3_CUSTOM_DOMAIN}/'

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

            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },

        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }