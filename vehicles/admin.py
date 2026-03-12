from django.contrib import admin
from .models import Vehicle, VehicleType


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'license_plate', 'color']
    search_fields = ['model', 'license_plate']
    list_filter = ['vehicle_type']


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
