from django.apps import AppConfig


class MomoDevcAppConfig(AppConfig):
    name = 'momo_devc_app'

    def ready(self):
        import momo_devc_app.signals
