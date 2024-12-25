from mysite.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%0z$4!^er4as49f(+f%qdh(^c&!+$ddob9$6#_f5cq%pv%4)@l'

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = []

#page 404
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
# DEBUG = False
# TEMPLATE_DEBUG = DEBUG
# ALLOWED_HOSTS = ["*"]


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts


#capcha
# https://pylessons.com/django-recaptcha
RECAPTCHA_PUBLIC_KEY = '6Lcp9ZsqAAAAALjIpdP2F4Q2nfLBdFxOXb3vXw7R'
RECAPTCHA_PRIVATE_KEY = '6Lcp9ZsqAAAAANPakRQQjU7wqo2n4hAiNLTrRQhT' 
 

#sites
SITE_ID = 2





DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': str(BASE_DIR / 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'postgresdb',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',  
    },
}

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
STATIC_ROOT= BASE_DIR/'static'
MEDIA_ROOT = BASE_DIR / 'media'


