# Django settings for strategchen project.

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Susann Jenkner', 'info@strategchen.com'),
    ('Stefan Jenkner', 'stefan@jenkner.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'strategchen.db',       # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Collected static files
STATIC_ROOT = os.path.join(BASE_DIR, 'sitestatic')
#STATIC_ROOT = 'static'
STATIC_URL = '/static/'

# Additional static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Media Storage
AWS_S3_FILE_OVERWRITE = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_HEADERS = {
#    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}
from boto.s3.connection import OrdinaryCallingFormat
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'

MEDIA_URL = 'http://%s/' % AWS_STORAGE_BUCKET_NAME
#MEDIA_URL = 'https://s3-eu-west-1.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
#MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'

# http://django-imagekit.readthedocs.org/en/latest/configuration.html
IMAGEKIT_CACHEFILE_DIR = 'cache/images'
IMAGEKIT_CACHE_BACKEND = 'default'
IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = 'imagekit.cachefiles.strategies.Optimistic'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w=!f@&2n-573my!76!jkzw*=ajp8z#srx-f31yi9+bdp6^$np9'

# Login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    #'blog.middleware.FeedburnerMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'strategchen.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/simple'
MARKITUP_PREVIEW_FILTER = ('markdown.markdown', {'safe_mode': True})

ROBOTS_CACHE_TIMEOUT = 60*60*24

DISQUS_API_KEY = 'hEUEmL8u2AeCfH7W2d1k99lDJBS0KIuIaZ7anGjfeYbiq3Wyrhs6LxjpNtq9b0EK'
DISQUS_WEBSITE_SHORTNAME = 'strategchen'

FEEDBURNER_URLS = {
    '/feeds/atom/': 'http://feeds.feedburner.com/StrategchenBlog',
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.syndication',
    'storages',
    'disqus',
    'reversion',
    'blog',
    'flatpages',
    'markitup',
    'tagging',
    'robots',
    'imagekit',
    'basic.media',
    'basic.inlines',
)
