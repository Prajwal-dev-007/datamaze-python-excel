"""
Django settings for datamaze project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3bhla@2639y1l_4bf^2*d162$kk6k-^qtgb=zb=r8$+2+2+du#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_beat',
    'corsheaders',
    'webpack_loader',
    'home',
   

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'datamaze',      # Replace with your database name
        'USER': 'postgres',      # Replace with your PostgreSQL username
        'PASSWORD': 'Mike@007',       # Replace with your PostgreSQL password
        'HOST': 'localhost',               # Or the IP address where your PostgreSQL is hosted
        'PORT': '5432',                    # Default PostgreSQL port
    }
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 70485760  # 10MB, adjust as needed
FILE_UPLOAD_MAX_MEMORY_SIZE = 70485760  # 10MB, adjust as needed

# settings.py

# Celery Configuration Options
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis as the message broker
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Redis to store task results

# Optional: Use JSON for task serialization
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Optional: Set the timezone and enable UTC
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

# Optional: Control task expiry
CELERY_TASK_TIME_LIMIT = 3600  # 1 hour (adjust as needed)

CELERY_TASK_ROUTES = {
    'my_app.tasks.process_excel_file_task': {'queue': 'excel_tasks'},
}

CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
CELERYD_TASK_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# settings.py

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# settings.py

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'




ROOT_URLCONF = 'datamaze.urls'
CORS_ALLOW_ALL_ORIGINS = True 
ALLOWED_HOSTS = ['your-django-backend.com', 'localhost', '127.0.0.1']



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'datamaze.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.sqlite3',
  #      'NAME': BASE_DIR / 'db.sqlite3',
  #  }/*
#}


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

# settings.py
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',  # Directory inside your static folder where bundles will be stored
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),  # Path to Webpack's stats file
    }
}


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
