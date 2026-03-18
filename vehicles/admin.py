from django.contrib import admin
from .models import Brand, Color, Model, Vehicle, VehicleType


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'license_plate', 'color']
    search_fields = ['model', 'license_plate']
    list_filter = ['vehicle_type']


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
