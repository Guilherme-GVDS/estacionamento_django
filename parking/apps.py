from django.apps import AppConfig


class ParkingConfig(AppConfig):
    name = 'parking'
    verbose_name = 'Estacionamento'

    def ready(self):
        import parking.signals  # Importa os sinais para garantir que sejam registrados
