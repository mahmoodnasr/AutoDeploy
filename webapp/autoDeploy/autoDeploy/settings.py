"""
Django settings for autoDeploy project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o+=n$-ko25kx^30b(rm#_xwoz9&#r9_$p8p=qza79ida8etb)#'

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

    'django_tables2',
    'django_tables2_reports',

    'accounts',
    'mfa',
    'deployment',
    'integration',
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

ROOT_URLCONF = 'autoDeploy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "accounts/templates"),
            os.path.join(BASE_DIR, "deployment/templates"),
            os.path.join(BASE_DIR, "integration/templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'autoDeploy.processor.global_settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'autoDeploy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autodeploy',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',  # 127.0.0.1
        'port': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TITLE = "autoDeploy"

BASE_URL = "/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = BASE_URL+ 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "my_static"),
)
STATIC_ROOT=BASE_DIR+'/static/'

PROJECTS_DIR='/opt/autodeploy/projects/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = BASE_URL + 'media/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 30000  # time in seconds

LOGIN_URL=BASE_URL+"accounts/login"

EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER= ''
EMAIL_HOST_PASSWORD=''
EMAIL_USE_TLS=True
EMAIL_FROM="AutoDeploy"


MFA_UNALLOWED_METHODS=()   # Methods that shouldn't be allowed for the user
MFA_LOGIN_CALLBACK="accounts.views.log_user_in"            # A function that should be called by username to login the user in session
MFA_RECHECK=True           # Allow random rechecking of the user
MFA_RECHECK_MIN=10         # Minimum interval in seconds
MFA_RECHECK_MAX=30         # Maximum in seconds
MFA_QUICKLOGIN=True        # Allow quick login for returning users by provide only their 2FA

TOKEN_ISSUER_NAME="Auto Deploy"      #TOTP Issuer name

U2F_APPID="https://localhost"    #URL For U2F
FIDO_SERVER_ID="localhost"      # Server rp id for FIDO2
FIDO_SERVER_NAME="Autodeploy"
FIDO_LOGIN_URL=BASE_URL