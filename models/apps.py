from django.apps import AppConfig


class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models'

    # def ready(self):
    #     # 시그널 등록 등이 필요할 때만
    #     from . import user_models
