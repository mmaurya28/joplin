"""
Django settings for joplin project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from distutils.util import strtobool

import dj_database_url
from django.conf import global_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


DEBUG = bool(strtobool(os.environ.get('DEBUG', str(False))))
MODELTRANSLATION_DEBUG = DEBUG
USE_ANALYTICS = bool(strtobool(os.environ.get('USE_ANALYTICS', str(not DEBUG))))


# Application definition

INSTALLED_APPS = [
    'base.apps.BaseConfig',
    'users',
    'api.apps.APIConfig',

    'wagtail.api.v2',

    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',

    'modelcluster',
    'taggit',
    'rest_framework',
    'corsheaders',
    'modeltranslation',
    'graphene_django',
    'django_extensions',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'wagtail.contrib.modeladmin',
    'webpack_loader',
    'dbbackup',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': [
                'base.templatetags.joplin_tags',
            ],
            'context_processors': [
                'base.context_processors.settings_context',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Detect whether it is a staging or production environment
DEPLOYMENT_MODE = os.environ.get('DEPLOYMENT_MODE', 'LOCAL')
ISPRODUCTION = DEPLOYMENT_MODE == "PRODUCTION"
ISSTAGING = DEPLOYMENT_MODE == "STAGING"
ISREVIEWAPP = DEPLOYMENT_MODE == "REVIEW"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#
# dj_database_url should detect the environment variable 'DATABASE_URL',
# this is provided by Heroku in production, or locally via Dockerfile.local,
# if it does not, then assume SQLite.
#
default_db_url = f'sqlite:///{os.path.join(PROJECT_DIR, "db.sqlite3")}'
DATABASES = {
    'default': dj_database_url.config(default=default_db_url),
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en-us'
SUPPORTED_LANGS = (
    'en',
    'es',
    'vi',
    'ar',
)
LANGUAGES = [lang for lang in global_settings.LANGUAGES if lang[0] in SUPPORTED_LANGS]

TIME_ZONE = 'UTC'
USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'webpack_bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'joplin/static/webpack-stats.json'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'users.User'

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

if DEBUG:
    ALLOWED_HOSTS.append('*')


# Wagtail settings

WAGTAIL_SITE_NAME = 'joplin'
WAGTAIL_AUTO_UPDATE_PREVIEW = True
WAGTAILIMAGES_IMAGE_MODEL = 'base.TranslatedImage'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://austintexas.io'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1iq1u6gs+xh3!bvrl-5$jqne%gpj)!wv5^h0$dc0y84xsdr-95'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

HEROKU_KEY = os.getenv('HEROKU_KEY')
HEROKU_JANIS_APP_NAME = os.getenv('HEROKU_JANIS_APP_NAME')
JANIS_URL = os.getenv('JANIS_URL', 'http://localhost:3000')

GRAPHENE = {
    'SCHEMA': 'api.schema.schema',
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ]
}


# Assume DB default settings for LOCAL env
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/app/joplin/db/backups'}

# Production, Staging & Review Apps
if(ISPRODUCTION or ISSTAGING):
    #
    # AWS Buckets only if not local.
    #
    APPLICATION_NAME = os.getenv('APPLICATION_NAME')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_S3_KEYID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_S3_ACCESSKEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_S3_BUCKET')
    AWS_ARCHIVE_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_ARCHIVE')
    AWS_BACKUPS_LOCATION = os.getenv('AWS_S3_BUCKET_ARCHIVE_LOCATION')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # We now change the backups directory
    DBBACKUP_STORAGE_OPTIONS = {
        'access_key': AWS_ACCESS_KEY_ID,
        'secret_key': AWS_SECRET_ACCESS_KEY,
        'bucket_name': AWS_ARCHIVE_BUCKET_NAME,
        'host': "s3.amazonaws.com",
        'location': AWS_BACKUPS_LOCATION + "/" + APPLICATION_NAME
    }

    # We now change the storage mode to S3 via Boto for default, static and dbbackup
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

