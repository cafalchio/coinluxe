from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEGUB')

ALLOWED_HOSTS = ['www.coinluxe.cafabr.online', 'localhost', '127.0.0.1']

INTERNAL_IPS = [
    "127.0.0.1",
]

TAILWIND_APP_NAME = "theme"
TAILWIND_DEV_MODE = DEBUG
TAILWIND_CSS_FILE = "theme/static/css/syles.css"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'theme',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # tailwind
    'tailwind',
    "crispy_forms",
    "crispy_tailwind",

    # allauth
    "allauth_ui",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "widget_tweaks",
    # storage s3
    'storages',
    'api_backend',
    'portifolio',
    'products',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coinluxe.urls'

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'theme', 'templates'),
            os.path.join(BASE_DIR, 'theme', 'templates', 'allauth'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'theme.context_processor.theme',  # https://www.youtube.com/watch?v=K1e8kpoag0E
                'portifolio.context_processors.credits',
            ],
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = "webcoinluxe.gmail.com"
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'webcoinluxeshop@gmail.com'
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'coinluxe.wsgi.application'

# DATABASE_URL = os.environ.get("DATABASE_URL")

# DATABASES = {
#     'default': dj_database_url.parse(DATABASE_URL)
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_USER_PASS'),
        'HOST': 'localhost',  # Replace with your PostgreSQL server's address if necessary
        # Leave empty to use the default PostgreSQL port (usually 5432)
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'theme', 'static'),
]
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, 'media'),
]
MEDIA_URL = "/media/"
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SAVE_PICS = os.path.join(BASE_DIR, 'media', 'coin_pics')

# if 'USE_AWS' in os.environ:
#     AWS_S3_OBJECT_PARAMETERS = {
#         'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#         'CacheControl': 'max-age=94608000',
#     }
#     AWS_STORAGE_BUCKET_NAME = 'coinluxe'
#     AWS_S3_REGION_NAME = 'eu-west-1'
#     AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

#     # Static and media files
#     STATICFILES_STORAGE = 'custom_storages.StaticStorage'
#     STATICFILES_LOCATION = 'static'
#     DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#     MEDIAFILES_LOCATION = 'media'

#     # Override static and media URLs in production
#     STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
#     MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_PUBLIC_KEY_TEST = os.environ.get("STRIPE_PUBLIC_KEY_TEST")
STRIPE_SECRET_KEY_TEST = os.environ.get("STRIPE_SECRET_KEY_TEST")
STRIPE_WEBHOOK_SECRET_TEST = os.environ.get("STRIPE_WEBHOOK_SECRET_TEST")
REDIRECT_DOMAIN = "https://coinluxe.herokuapp.com/portifolio"

PRODUCT_PRICE = "price_1NHoiiHDQ21gOZTqjAwPDuLt"

SITE_NAME = 'Coinluxe'

# dealing wit warnings in python manage.py check --deploy
# if not DEBUG:
#     SECURE_HSTS_SECONDS = 31536000 * 2
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#     CSRF_COOKIE_SECURE = True
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
