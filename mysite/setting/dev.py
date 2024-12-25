from mysite.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%0z$4!^er4as49f(+f%qdh(^c&!+$ddob9$6#_f5cq%pv%4)@l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#capcha
# https://pylessons.com/django-recaptcha
RECAPTCHA_PUBLIC_KEY = '6Lcp9ZsqAAAAALjIpdP2F4Q2nfLBdFxOXb3vXw7R'
RECAPTCHA_PRIVATE_KEY = '6Lcp9ZsqAAAAANPakRQQjU7wqo2n4hAiNLTrRQhT' 
 

#authentication
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = "blogofficiall9@gmail.com"

EMAIL_HOST_PASSWORD = "kkvs jzgr alve lixm"

#sites
SITE_ID = 2


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
STATIC_ROOT= BASE_DIR/'static'
MEDIA_ROOT = BASE_DIR / 'media'


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




