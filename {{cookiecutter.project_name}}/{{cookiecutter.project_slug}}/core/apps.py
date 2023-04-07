from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{cookiecutter.project_slug}}.core'
    
    # def ready(self) -> None:
    #     import {{cookiecutter.project_slug}}.core.signals.handlers