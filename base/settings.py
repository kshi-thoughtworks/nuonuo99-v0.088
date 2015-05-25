#coding:utf-8
"""
Django settings for base project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aurxubv)48jyi$(yfc&wf4mz$13-q$)05t1siz-8fv^tj*__v*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

project_app = (
    'base',  # 基础类
    'accounts',  # 用户账号
    'provider',  # 供应商
    'location',  # 位置信息
    'expert',  # 婚礼人
    'std_product',  # 单品
    'wedding',  # 婚礼信息/购物车/订单
    # 'space',  # 场地
    )


ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# ------------- DEV settings. DEBUG = TRUE --------------------

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ------------- DEV settings. END ------------------------------


# ------------- DEPLOY settings. DEBUG = FALSE ------------------------------

if not DEBUG:

    TEMPLATE_DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
            }
        }

# ------------- DEPLOY settings. END ------------------------------

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'guardian',
    'userena',
    'crispy_forms',
    'reversion',
    'xadmin',
) + project_app

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'base.urls'

WSGI_APPLICATION = 'base.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

project_static = tuple([os.path.join(BASE_DIR, '%s/static' % app_name) for app_name in project_app])

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "base/static"),
) + project_static


project_template = tuple([os.path.join(BASE_DIR, '%s/templates' % app_name) for app_name in project_app])

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'base/templates'),
) + project_template


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
AVATAR_PATH = "avatar_photo"  # 头像相册
DEMO_PATH = "demo_photo"
SERVICE_PATH = "service_photo"  # 服务效果图片
PRODUCT_PATH="product_photo"  # 单品效果图片
WEDDING_CASE_PATH="wedding_case_photo"  # 婚礼案例/作品库图片
SPACE_PATH="space_photo"


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)


ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'accounts.MyProfile'
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
USERENA_ACTIVATION_REQUIRED = False


try:
    from local_settings import *
except Exception as e:
    pass
