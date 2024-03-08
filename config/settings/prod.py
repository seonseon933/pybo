import environ
from .base import *

ALLOWED_HOSTS = ['3.37.251.246']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = [] 
# ~_ROOT가 설정된 경우 STA~_DIR 리스트에 ~_ROOT와 동일한 디렉터리가 
# 포함되어 있으면 서버 실행 시 오류나서 그럼. 그러니 빈 칸으로.
DEBUG = False

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}