"""
Django settings for printlock project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pathlib import Path
import  os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.core.management import templates

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#%#&q*h2r564n0jsfb#2ra64+%jaw6(e#xy*n*qawgbzx&-x=1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*","15.207.253.230"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'storages',
    'printers',
    'rest_framework',
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

ROOT_URLCONF = 'printlock.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'printlock.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'NAME'      : 'Printolook_1',
        'USER'      : 'anup',
        'PASSWORD'  : 'Anup@123',
        'HOST'      :'localhost',
        'PORT'      : '3306',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD  = 'django.db.models.BigAutoField'

AUTH_USER_MODEL     = 'dashboard.User'

STATIC_URL          = '/static/'
STATICFILES_DIRS    = [os.path.join(BASE_DIR, "static")]
MEDIA_ROOT          = os.path.join(BASE_DIR, 'media')
STATIC_ROOT         = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL           = '/media/'


EMAIL_BACKEND        = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST           = 'smtp.gmail.com'
EMAIL_PORT           = '587'
EMAIL_HOST_USER      = 'moin46606@gmail.com'
EMAIL_HOST_PASSWORD  = '9934294473'
EMAIL_USE_TLS        = True



# AWS_STORAGE_BUCKET_NAME = 'bookeeda'
# AWS_ACCESS_KEY_ID = 'AKIAWKG6OT5Q6GXUWYVW'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# STATICFILES_LOCATION = 'staticold'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
# STATICFILES_STORAGE = 'custom_storage.StaticStorage'

# MEDIAFILES_LOCATION = 'media/Product'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'