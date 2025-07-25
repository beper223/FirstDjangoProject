"""
Django settings for MyDjangoProject project.

Generated by 'django-admin startproject' using Django 5.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

import src.firstapp.apps
from environ import Env
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local
    'src.firstapp.apps.FirstappConfig',
    'src.library.apps.LibraryConfig',
    'src.taskmanager.apps.TaskmanagerConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # отвечает за безопасность
    # добавляет пару заголовков, позволяет работать HTTPS
    'django.contrib.sessions.middleware.SessionMiddleware', # принимает данные и при необходимости передает в другие запросы
    'django.middleware.common.CommonMiddleware', # для работы с эндпоинтами, добавляет / если пользователь не указал
    # так же добавляет спецсимволы (заменяет пробелы)
    'django.middleware.csrf.CsrfViewMiddleware', # защита от атак csrf (межсайтовая атака)
    'django.contrib.auth.middleware.AuthenticationMiddleware', # помогает определять юзера, работающего на сайте
    'django.contrib.messages.middleware.MessageMiddleware', # помогает управлять служебными сообщениями
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # защита от кликхакинга (прозрачные фреймы)
    # добавляет специальный заголовок
    # local
    'src.firstapp.middleware.CustomMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

if env.bool('USE_REMOTE_DB'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': env.str('DB_NAME'),
            'HOST': env.str('DB_HOST'),
            'PORT': env.int('DB_PORT'),
            'USER': env.str('DB_USER'),
            'PASSWORD': env.str('DB_PASSWORD'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # проверяет пароль на данные юзера (пароль не должен дублировать имя пользователя)
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',# задает минимальную длину пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',# проверить пароль на слишком популярные или простые пароли
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',# помогает проверить, что пароль состоит из букв и цифр, и что пароль не содержит только цифры
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
