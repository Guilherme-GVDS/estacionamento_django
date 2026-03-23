from django.db import models
from vehicles.models import Vehicle


class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Número da Vaga'
    )
    is_occupied = models.BooleanField(default=False, verbose_name='Ocupada')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criada em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizada em'
    )

    class Meta:
        verbose_name = 'Vaga de Estacionamento'
        verbose_name_plural = 'Vagas de Estacionamento'
        ordering = ['spot_number']

    def __str__(self):
        return self.spot_number


class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        verbose_name='Veículo',
        related_name='parking_records',
    )
    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        verbose_name='Vaga',
        related_name='parking_records',
    )
    entry_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Hora de Entrada'
    )
    exit_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Hora de Saída'
    )

    class Meta:
        verbose_name = 'Registro de Estacionamento'
        verbose_name_plural = 'Registros de Estacionamento'
        ordering = ['-entry_time']

    def __str__(self):
        return f'{self.vehicle} | Vaga {self.parking_spot} | {self.entry_time}'
