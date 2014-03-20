#coding:utf8
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.conf import settings
"""
Django settings for lxmagic project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p=$%^t#lr051lwo@_0h#&dr@e@f)gahescsiote)el7ks%ag!)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'banner',
    'product',
    'news',
    'menu',
    'redactor',
    'mptt',
    'smart_selects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'product.processors.get_parent_categories',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

ROOT_URLCONF = 'lxmagic.urls'

WSGI_APPLICATION = 'lxmagic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lxmagic',
        'USER': 'jazdelu',
        'PASSWORD': 'lushizhao1129'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


STATIC_ROOT = os.path.join(BASE_DIR, 'static/'),

STATIC_URL = '/static/'
MEDIA_URL = ' /u/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'u/'),

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)
# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'LXMAGIC Website Manager',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'MENU':(
        {'app':'auth','label':u'用户管理','icon':'icon-user'},
        {'app':'banner','label':u'幻灯片管理','icon':'icon-picture'},
        {'app':'product','label':u'产品管理','icon':'icon-shopping-cart'},
        {'app':'news','label':u'活动管理','icon':'icon-edit'},
        {'app':'menu','label':u'菜单管理','icon':'icon-bookmark'},
    ),
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'banner': 'icon-play',
        'auth': 'icon-user',
     },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),


    # misc
    'LIST_PER_PAGE': 15
} 'LIST_PER_PAGE': 15
}
#Redactor Settings
REDACTOR_OPTIONS = {'lang': 'zh'}
REDACTOR_UPLOAD = 'u/'
