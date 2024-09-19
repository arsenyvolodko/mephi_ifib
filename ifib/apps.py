from django.apps import AppConfig


class IfibConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ifib"

    def ready(self):
        import ifib.signals
