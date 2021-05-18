from pathlib import Path
import os
import dj_database_url #追加
from socket import gethostname
# import django_heroku
hostname = gethostname()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SERECT_KEY = 'PBqvJSws8A49cHfCJiU1GDw8h1cW1z6JChGzTpA6'
SECRET_KEY = 'django-insecure-kb&$1c(cu*8(67(fu5168w5lihgnzvq)srl_6)4o-hzm8)m5vo'


# SECURITY WARNING: don't run with debug turned on in production!
# 開発環境ならTrue
# DEBUG = True
# 本番ならFalse
DEBUG = False

ALLOWED_HOSTS = ['marioshareapp.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'marioshareapp',
    'embed_video',
    #'django_cleanup.apps.CleanupConfig',
    #'storages'
]


#AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
#AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
#AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#MEDIA_URL = S3_URL

#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = None


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MarioShare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'marioshareapp.context.related',
            ],
        },
    },
]

WSGI_APPLICATION = 'MarioShare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#if "COMPUTER-NAME" in hostname:
    # デバッグ環境
    # DEBUG = True 
#DATABASES = {
#      'default': {
#           'ENGINE': 'django.db.backends.sqlite3',
#           'NAME': 'db.sqlite3',
#       }
#   }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'marioshareapp',
        'USERNAME':'Juvenile',
        'PASSWORD':'MarioShareapp',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'marioshareapp.herokuapp.com'] 
#else:
    # 本番環境
    # DEBUG = False
 #   db_from_env = dj_database_url.config()
 #   DATABASES = {
 #       'default': dj_database_url.config()
 #   }
 #   ALLOWED_HOSTS = ['*']


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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# 本番環境ならこっちが必要？
STATIC_ROOT = BASE_DIR / 'static'
# 開発環境で調べたいならここは必要。
# STATICFILES_DIRS = [str(BASE_DIR / 'static')]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

#if not DEBUG:
#    SECRET_KEY = os.environ['SECRET_KEY']

#    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
#    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
#    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

#    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#    MEDIA_URL = S3_URL

#    AWS_S3_FILE_OVERWRITE = False
#    AWS_DEFAULT_ACL = None

#    django_heroku.settings(locals())

#db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
#DATABASES['default'].update(db_from_env)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
