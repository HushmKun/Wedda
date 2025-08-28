from pathlib import Path
from os import environ, getenv
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('SECRET_KEY', "QWERTyoP[poIuytRewASdfgHJkL;?.<mnBvcXzxCvbNm,./;lkJhgFdSWQErtYui]")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ.get('DJANGO_DEBUG', 'True') == 'True'    

ALLOWED_HOSTS = environ.get('DJANGO_HOSTS', '*').split(',')

if DEBUG : 
    ALLOWED_HOSTS.append('*')

# Application definition
DJANGO_APPS =  [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps'
]

VENDOR_APPS = [
    "admin_interface",
    "colorfield",
]

THIRD_PARTY_APPS = [
    'main'
]

INSTALLED_APPS =  VENDOR_APPS + DJANGO_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wedda.urls'

SITE_ID = 1 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            CONTENT_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wedda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': CONTENT_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

LOCALE_PATHS = (CONTENT_DIR / 'locale',)

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
]

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    CONTENT_DIR / "static"
]

STATIC_ROOT = '/home/afmstjbq/public_html/static/'


MEDIA_ROOT = '/home/afmstjbq/public_html/media/'

MEDIA_URL = 'media/'

if DEBUG:
    
    # STATICFILES_DIRS = [r"D:\Code\Templates\Web\qutiiz-digital-marketing-agency-html-template-2024-03-22-06-28-18-utc\qutiiz-package-26-05-2022\qutiiz-html-files\assets"]
    MEDIA_ROOT = CONTENT_DIR / 'media'
    MEDIA_URL = 'media/'
    
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

EMAIL_BACKEND = getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = getenv("EMAIL_HOST", "wedda.agency")
EMAIL_PORT = int(getenv("EMAIL_PORT", 465))
EMAIL_USE_TLS = getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD", "")
