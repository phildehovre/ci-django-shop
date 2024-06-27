from .base import *

ALLOWED_HOSTS = ['django-shop.up.railway.app','127.0.0.1', 'localhost']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AWS_LOCATION="django_shop"

if config("DJANGO_ENVIRONMENT")  == "production":
    # This determines the location of the files the app will source.
    STATIC_URL = f'{AWS_S3_URL_PROTOCOL}//{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

    # This determines where the files will be uploaded
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
            "LOCATION": AWS_LOCATION
        },

        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
            "LOCATION": AWS_LOCATION
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