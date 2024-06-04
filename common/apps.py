from django.apps import AppConfig
from django.db.models import BigAutoField


class CommonConfig(AppConfig):
    name = 'common'
    default_auto_field = 'django.db.models.BigAutoField'
