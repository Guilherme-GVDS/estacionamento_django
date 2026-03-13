from django.db import models
from customers.models import Customer


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Marca')

    class Meta:
        verbose_name = 'Marca do Veículo'
        verbose_name_plural = 'Marcas dos Veículos'

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Modelo')

    class Meta:
        verbose_name = 'Modelo do Veículo'
        verbose_name_plural = 'Modelos dos Veículos'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='Cor')

    class Meta:
        verbose_name = 'Cor do Veículo'
        verbose_name_plural = 'Cor dos Veículos'

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Nome'
        )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Descrição'
        )

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Proprietário',
        related_name='vehicles',
    )
    license_plate = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Placa'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Marca',
        related_name='vehicles',
    )
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Tipo do Veículo',
        related_name='vehicles',
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Modelo',
        related_name='vehicles',
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Cor',
        related_name='vehicles',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.license_plate
