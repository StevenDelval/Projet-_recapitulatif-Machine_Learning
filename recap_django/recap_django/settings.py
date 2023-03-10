"""
Django settings for recap_django project.
Generated by 'django-admin startproject' using Django 4.0.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/topics/settings/
"""

#import dj_database_url
import os
from django.test.runner import DiscoverRunner
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2=p)b=1m)*@6&r5#bihf(w464ldc#1^@z)kpl731zrlxq1pa3('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["0.0.0.0","51.11.205.197","django-sbec.dgg8fne4dzgpdjc5.francecentral.azurecontainer.io"]
CSRF_TRUSTED_ORIGINS = ["http://django-sbec.dgg8fne4dzgpdjc5.francecentral.azurecontainer.io"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'widget_tweaks',
    'crispy_forms',
    "crispy_tailwind",
    'base',
    # Ajouter les applications
    
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "recap_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates' ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "recap_django.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

MAX_CONN_AGE = 600

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3")
#     }
# }






DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DB_USERNAME = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_DATABASE = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_AVAILABLE = all(   #use any name in place of POSTGRES_AVAILABLE
    [DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT]
)
try:
    POSTGRES_RDY = int(os.getenv('POSTGRES_RDY'))
except:
    POSTGRES_RDY = 0

if POSTGRES_AVAILABLE and POSTGRES_RDY:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_DATABASE,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}  








# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'base/static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Enable WhiteNoise's GZip compression of static assets.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Test Runner Config
class HerokuDiscoverRunner(DiscoverRunner):
    """Test Runner for Heroku CI, which provides a database for you.
    This requires you to set the TEST database (done for you by settings().)"""

    def setup_databases(self, **kwargs):
        self.keepdb = True
        return super(HerokuDiscoverRunner, self).setup_databases(**kwargs)


# Use HerokuDiscoverRunner on Heroku CI
if "CI" in os.environ:
    TEST_RUNNER = "recap_django.settings.HerokuDiscoverRunner"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = "base.User"
