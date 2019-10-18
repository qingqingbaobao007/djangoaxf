"""
Django settings for axf project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=z=au=dsc+9qwdv9e2dm&iu05+b$_8%%$te*eo(*ivr@eup*-w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HomeApp',
    'MarketApp',
    'CartApp',
    'MineApp',
    'UserApp',
    'OrderApp',
    'debug_toolbar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'axf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'axf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'axf1905',
        'USER':'mimi',
        'PASSWORD':'123',
        'HOST':'localhost',
        'PORT':3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

MEDIA_ROOT = os.path.join(BASE_DIR,'static/upload')

EMAIL_HOST='smtp.qq.com'
EMAIL_PORT=465
EMAIL_HOST_USER='738613409@qq.com'
EMAIL_HOST_PASSWORD='cpjvcyjluxizbcic'
EMAIL_USE_LLS=True
EMAIL_FROM='738613409@qq.com'


CACHES={
                    'default':{
                        'BACKEND':'django_redis.cache.RedisCache',
                        'LOCATION':'redis://127.0.0.1:6379/1',
                        'OPTIONS':{
                                'CLIENT_CLASS':'django_redis.client.DefaultClient'
                        }
                    }
                }
FONT_PATH = os.path.join(BASE_DIR,'static/fonts/ADOBEARABIC-BOLD.OTF')


APP_PRIVATE_KEY_STRING=open(os.path.join(BASE_DIR,'alipay_config/app_rsa_private_key.pem'),'r').read()

ALIPAY_PUBLIC_KEY_STRING=open(os.path.join(BASE_DIR,'alipay_config/alipay_rsa_public_key.pem'),'r').read()

INTERNAL_IPS=('127.0.0.1')