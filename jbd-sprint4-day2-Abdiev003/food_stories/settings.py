"""
Django settings for food_stories project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1v*a0pr6it4)wcfzz943-)rs!*pfd)ah$y&e-&8-j_rou5f5*h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get('DEBUG') else True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'accounts.User'

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party packages
    'ckeditor',
    'ckeditor_uploader',
    'social_django',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_celery_beat',


    # custom apps
    'stories.apps.StoriesConfig',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'food_stories.middleware.force_default_middleware.force_default_language_middleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

    'stories.middleware.BlackListIPMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ROOT_URLCONF = 'food_stories.urls'

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

                'django.template.context_processors.i18n',
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',  # <--
            ],
        },
    },
]

CELERY_BROKER_URL = f'redis://{os.environ.get("REDIS_HOST", "localhost")}:6379'
CELERY_RESULT_BACKEND = f'redis://{os.environ.get("REDIS_HOST", "localhost")}:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku'

WSGI_APPLICATION = 'food_stories.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'db_name'),
        'USER': os.environ.get('POSTGRES_USER', 'user_name'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '12345'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432)
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'az'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'stories.utils.ckeditor_files.get_filename'
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_DATE = True

CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        "width": '100%'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # BASE_DIR / "static",


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ugettext = lambda s: s

LANGUAGES = (
    ('en', ugettext('English')),
    ('ru', ugettext('Russia')),
    ('az', ugettext('Azerbaijan')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

# JET CONFIGs
JET_DEFAULT_THEME = 'light-gray'
JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

LOGIN_URL = reverse_lazy('accounts:login')
LOGIN_REDIRECT_URL = reverse_lazy('stories:index')
LOGOUT_URL = reverse_lazy('accounts:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('stories:index')

SOCIAL_AUTH_FACEBOOK_KEY = '169164915044824'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '336214ce573b5f31df21e345ae037143'  # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_friends']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email,picture',
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '360419868722-ulm9n2tok5lsmiin5psv75it4l2jp9ov.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'TUxQnlu3xpYPNijrYAtzcA2D'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'accounts.tools.social_auth.update_user_social_data',  # custom pipeline
)

# email details
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'techacademy2021@gmail.com'
EMAIL_HOST_PASSWORD = 'nxjlrlzznwuhynst'

SITE_ADDRESS = 'http://localhost:8000'
