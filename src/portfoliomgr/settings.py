"""
Django settings for portfoliomgr project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uuoc10!bp#0bkgq2oyh3s@sd^8%^k3(q8poba@onqv)@9zy(*4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] if DEBUG==False else [ ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
    'huey.contrib.djhuey',
    # own
    'ppf',
    'ssy',
    'epf',
    'espp',
    'rsu',
    'goal',
    'users',
    'shares',
    'mutualfunds',
    'fixed_deposit',
    'reports',
    'common',
    'calculator',
    'tasks',
    'alerts',
    'pages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfoliomgr.urls'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "ppf"),
    os.path.join(BASE_DIR, "ssy"),
    os.path.join(BASE_DIR, "epf"),
    os.path.join(BASE_DIR, "espp"),
    os.path.join(BASE_DIR, "shares"),
    os.path.join(BASE_DIR, "goal"),
    os.path.join(BASE_DIR, "mutualfunds"),
    os.path.join(BASE_DIR, "fixed_deposit"),
    os.path.join(BASE_DIR, "rsu"),
    os.path.join(BASE_DIR, "users"),
    os.path.join(BASE_DIR, "reports"),
    os.path.join(BASE_DIR, "common"),
    os.path.join(BASE_DIR, "calculator"),
    os.path.join(BASE_DIR, "alerts"),
    os.path.join(BASE_DIR, "pages"),
    os.path.join(BASE_DIR, "tasks"),
    os.path.join(BASE_DIR, "static"),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'template_filters': 'portfoliomgr.template_filters',

            }
        },
    },
]

WSGI_APPLICATION = 'portfoliomgr.wsgi.application'
ASGI_APPLICATION = "portfoliomgr.routing.application"

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

HUEY = {
    'huey_class': 'huey.SqliteHuey',
    'name': DATABASES['default']['NAME'],
    'results': True,  # Store return values of tasks.
    'store_none': False,  # If a task returns None, do not save to results.
    'immediate': False,
    'consumer': {
        'workers': 1,
        'worker_type': 'thread',
        'initial_delay': 0.1,  # Smallest polling interval, same as -d.
        'backoff': 1.15,  # Exponential backoff using this rate, -b.
        'max_delay': 10.0,  # Max possible polling interval, -m.
        'scheduler_interval': 1,  # Check schedule every second, -s.
        'periodic': True,  # Enable crontab feature.
        'check_worker_health': True,  # Enable worker health checks.
        'health_check_interval': 1,  # Check worker health every second.
    },
}
# Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')