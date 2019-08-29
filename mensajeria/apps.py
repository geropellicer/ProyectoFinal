from django.apps import AppConfig


class MensajeriaConfig(AppConfig):
    name = 'mensajeria'
    
    def ready(self):
        import mensajeria.signals