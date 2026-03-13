from django.apps import AppConfig


class ParkingConfig(AppConfig):
    name = 'parking'
    verbose_name = 'Estacionamento'

    def ready(self):
        import parking.signals  # noqa: F401
