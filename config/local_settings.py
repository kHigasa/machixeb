from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'machix_dev',
        'USER': 'andre',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
        'ATOMIC_REQUESTS': True,
    }
}
