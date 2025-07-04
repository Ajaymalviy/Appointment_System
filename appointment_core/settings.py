"""
Django settings for main_file_project project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/


For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
# import pdb 

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn='https://4724542625b18f74686b82a21bba479e@o4507298582429696.ingest.us.sentry.io/4507298585968640',
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0  # Set to 1.0 to capture 100% of transactions
# )



# sentry_sdk.init(
#     dsn="https://3d03a0d34b11be7caef5602ffe501090@o4507288658182144.ingest.us.sentry.io/4507288664014848",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )    


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR=os.path.join(BASE_DIR, "templates")


# STATIC_URL = '/static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     "/first_app_for_project/templates/static",
# ] 



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+06&o2#s%jjwokth(y694o)&azmei0sqtn*=cr(+ddo=*&wpr!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# ALLOWED_HOSTS = ['.vercel.app']
# settings.py
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

APPEND_SLASH = False

# Application definition

INSTALLED_APPS = [
    'appointments',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'sentry_sdk.integrations.django.middleware.SentryMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
  # 'allauth.account.middleware.AccountMiddleware',  # Add this line
   
  
]


ROOT_URLCONF = 'main_file_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'], 
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

WSGI_APPLICATION = 'main_file_project.wsgi.application'




# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'meetme',  # Specify the name of your MongoDB database
#         'ENFORCE_SCHEMA': False,  # Optional: Set to True if you want to enforce schema validation
#         'CLIENT': {
#             'host': 'mongodb://localhost:27017/',  # Specify the MongoDB connection URI
#         }
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'meetme',  # Your database name
#         'CLIENT': {
#             'host': os.getenv('mongodb+srv://ajeymalviya143:XoeezaNuVWudH0W9@cluster0.macr171.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'),
#             'username': os.getenv('ajeymalviya143'),
#             'password': os.getenv('XoeezaNuVWudH0W9'),
#             'authMechanism': 'SCRAM-SHA-1',
#         }
#     }
# }

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Print to verify environment variables are loaded (for debugging)
print("DB_NAME:", os.getenv('DB_NAME'))
print("DB_HOST:", os.getenv('DB_HOST'))
print("DB_USER:", os.getenv('DB_USER'))
print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('DB_NAME'),  # Database name
        'CLIENT': {
            'host': os.getenv('DB_HOST'),
            'username': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}


# import mongoengine
# mongoengine.connect(db='phone', host='localhost', username='root', password='password')
# DATABASES = {
# 'default': {
# 'ENGINE': 'djongo', #'django.db.backends.sqlite3',
# 'NAME': 'phone', # DB name
# 'USER': 'root', # DB User name <optional>
# }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # or False if you use SSL
EMAIL_HOST_USER = 'ajeymalviya143@gmail.com'
EMAIL_HOST_PASSWORD = 'yklm vyzm cmfo xyry'



# SOCIALACCOUNT_PROVIDERS = {
#         'google': {
#             'SCOPE' : [
#                 'profile',
#                 'email'
#             ],
#             'APP': {
#                 'client_id': '1013600742983-vub3nbfd4oqmlkqopfa4rnv8jatn0fnv.apps.googleusercontent.com',
#                 'secret': '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',
#             },
#             'AUTH_PARAMS': {
#                 'access_type':'online',
#             }
#         }
#     }

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend'
# ]
# SITE_ID = 2

# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'
    



