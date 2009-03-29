# Django settings for belleville project.
import os
import logging

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Barbara Shaurette', 'bshaurette@gmail.com'),
)
ADMIN_EMAIL = 'bshaurette@gmail.com'
MANAGERS = ADMINS

DATABASE_ENGINE = ''	    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''	    # Or path to database file if using sqlite3.
DATABASE_USER = ''              # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = '/Users/barbara/Code/belleville/site_media/'

# URL that handles the media served from MEDIA_ROOT
MEDIA_URL = 'http://127.0.0.1:8000/site_media/'

# URL prefix for admin media
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.project_logging.LoggingMiddleware',
)

ROOT_URLCONF = 'belleville.urls'

TEMPLATE_DIRS = (
    '/Users/barbara/Code/belleville/templates/', 
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.comments',
    'belleville.entry',
    'belleville.pages',
    'belleville.plugins',
    'belleville.plugins.books',
)

AKISMET_API_KEY = ''

LOGGING_LEVEL   = (logging.DEBUG if DEBUG else logging.WARNING)
# LOGGING_LOGFILE = os.path.join(os.environ['DJANGO_LOG_DIR'], DATABASE_NAME+'.log').replace('\\','/')
LOGGING_LOGFILE = '/Users/barbara/Code/logs/'+DATABASE_NAME+'.log'
LOGGING_FORMAT  = "%(asctime)s [%(levelname)s] %(message)s"
LOGGING_DATEFMT = "%m-%d %H:%M:%S"

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT,
                    datefmt=LOGGING_DATEFMT, filename=LOGGING_LOGFILE, filemode="a")


