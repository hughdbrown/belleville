# Django settings for belleville project.
import os
import os.path
import logging

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Barbara Shaurette', 'bshaurette@gmail.com'),
)
ADMIN_EMAIL = 'bshaurette@gmail.com'
MANAGERS = ADMINS

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

PROJECT_ROOT = '/Users/barbara/Code/belleville'
#This would work much better:
#PROJECT_ROOT = os.path.dirname(__file__)

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media/')

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
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.project_logging.LoggingMiddleware',
)

ROOT_URLCONF = 'belleville.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
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

try:
    from local_settings import *
except ImportError:
    print "Missing %s" % os.path.join(PROJECT_ROOT, "local_settings.py")

LOG_DIR = '/Users/barbara/Code/logs/'
# This would work a lot better:
#LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
LOGGING_LEVEL   = (logging.DEBUG if DEBUG else logging.WARNING)
# LOGGING_LOGFILE = os.path.join(os.environ['DJANGO_LOG_DIR'], DATABASE_NAME+'.log').replace('\\','/')
LOGGING_LOGFILE = os.path.join(LOG_DIR, DATABASE_NAME+'.log')
LOGGING_FORMAT  = "%(asctime)s [%(levelname)s] %(message)s"
LOGGING_DATEFMT = "%m-%d %H:%M:%S"

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT,
                    datefmt=LOGGING_DATEFMT, filename=LOGGING_LOGFILE, filemode="a")
