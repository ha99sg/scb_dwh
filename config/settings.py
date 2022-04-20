"""
Django settings for travel project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from django.utils.translation import gettext_lazy as _

from config.database import DATABASE
from config.root_local import LOCAL_ALLOWED_HOSTS  # noqa
from config.root_local import (
    LOCAL_DEBUG, LOCAL_EMAIL_HOST, LOCAL_EMAIL_HOST_PASSWORD,
    LOCAL_EMAIL_HOST_STRING, LOCAL_EMAIL_HOST_USER, LOCAL_EMAIL_PORT,
    LOCAL_EMAIL_USE_TLS, LOCAL_MEDIA_ROOT, LOCAL_SECRET_KEY, LOCAL_STATIC_ROOT,
    LOCAL_LDAP_SERVER, LOCAL_LDAP_DOMAIN
)
from library.constant.language import LANGUAGE_TYPE_ENGLISH

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LOCAL_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = LOCAL_DEBUG

ALLOWED_HOSTS = ['*']

# Application definition

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "drf_spectacular",
]
LOCAL_APPS = [
    "api",
    "core",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 3600,
    }
}

# if DEBUG:
#     INSTALLED_APPS += ['debug_toolbar', ]  # DEBUG Tool Bar
#     MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]  # DEBUG Tool Bar
#
#     # DEBUG Tool Bar
#     INTERNAL_IPS = ('127.0.0.1', '192.168.0.1',)
#     DEBUG_TOOLBAR_PANELS = [
#         'ddt_request_history.panels.request_history.RequestHistoryPanel',
#         'debug_toolbar.panels.versions.VersionsPanel',
#         'debug_toolbar.panels.timer.TimerPanel',
#         'debug_toolbar.panels.settings.SettingsPanel',
#         'debug_toolbar.panels.headers.HeadersPanel',
#         'debug_toolbar.panels.request.RequestPanel',
#         'debug_toolbar.panels.sql.SQLPanel',
#         'debug_toolbar.panels.templates.TemplatesPanel',
#         'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#         'debug_toolbar.panels.cache.CachePanel',
#         'debug_toolbar.panels.signals.SignalsPanel',
#         'debug_toolbar.panels.logging.LoggingPanel',
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#         'debug_toolbar.panels.profiling.ProfilingPanel',
#     ]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': DATABASE
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Ho_Chi_Minh'
DB_TIMEZONE = 'Asia/Ho_Chi_Minh'

LANGUAGES = (
    ('vi', 'VietNam'),
    ('en', 'English'),
)

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMAT = '%Y-%m-%d'
DATE_INPUT_FORMATS = (
    '%d/%m/%Y', '%d/%m/%Y', '%d/%m/%y',  # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',  # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',  # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',  # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',  # '25 October 2006', '25 October, 2006'
)

DATETIME_INPUT_OUTPUT_FORMAT = '%Y-%m-%d %H:%M:%S'

DATE_INPUT_OUTPUT_FORMAT = '%Y-%m-%d'

TIME_INPUT_OUTPUT_FORMAT = '%H:%M:%S'

DATETIME_FORMAT = 'd/m/Y H:i:s'
DATETIME_INPUT_FORMATS = (
    '%d/%m/%Y %H:%M:%S',  # '2006-10-25 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%d/%m/%Y %H:%M',  # '2006-10-25 14:30'
)

YEAR_MONTH_FORMAT = '%b/%Y'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_ROOT = LOCAL_MEDIA_ROOT
    STATIC_ROOT = LOCAL_STATIC_ROOT

# Mail
EMAIL_USE_TLS = LOCAL_EMAIL_USE_TLS
EMAIL_HOST = LOCAL_EMAIL_HOST
EMAIL_HOST_USER = LOCAL_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = LOCAL_EMAIL_HOST_PASSWORD
EMAIL_PORT = LOCAL_EMAIL_PORT
EMAIL_HOST_STRING = LOCAL_EMAIL_HOST_STRING

DEFAULT_LANGUAGE_ID = LANGUAGE_TYPE_ENGLISH

LAT = 16.088042
LON = 106.896973

DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000

# django-rest-framework
# -----------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DATETIME_FORMAT": DATETIME_INPUT_OUTPUT_FORMAT,
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_ALLOW_ALL_ORIGINS = True
CORS_URLS_REGEX = r"^/api/.*$"

# API documentation
# -----------------------------------------------------------------------------
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
SPECTACULAR_SETTINGS = {
    "TITLE": _("DWH API"),
    "DESCRIPTION": _("Documentation for DWH apis"),
    "VERSION": "",
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "displayOperationId": True,
    },
    'COMPONENT_SPLIT_REQUEST': True  # chuyển FileField về dạng chọn file binary
}

LDAP_SERVER = LOCAL_LDAP_SERVER
LDAP_DOMAIN = LOCAL_LDAP_DOMAIN

# SESSION
SESSION_COOKIE_AGE = 3600    # 60 minutes
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
