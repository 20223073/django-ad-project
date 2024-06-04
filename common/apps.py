from django.apps import AppConfig
from django.db.models import BigAutoField


class CommonConfig(AppConfig):
    name = 'common'

class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'