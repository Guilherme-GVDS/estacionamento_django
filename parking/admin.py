from django.contrib import admin

from vehicles.models import Vehicle
from .models import ParkingSpot, ParkingRecord


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied']
    search_fields = ['spot_number']
    list_filter = ['is_occupied']


@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'parking_spot', 'entry_time', 'exit_time']
    search_fields = ['vehicle__license_plate', 'parking_spot__spot_number']
    list_filter = ['entry_time', 'exit_time']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parking_spot':
            if not request.resolver_match.kwargs.get('object_id'):
                kwargs['queryset'] = ParkingSpot.objects.filter(
                    is_occupied=False
                )
        elif db_field.name == 'vehicle':
            if not request.resolver_match.kwargs.get('object_id'):
                parked_vehicles = ParkingRecord.objects.filter(
                    exit_time__isnull=True
                ).values_list('vehicle_id', flat=True)
                kwargs['queryset'] = Vehicle.objects.exclude(
                    id__in=parked_vehicles
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
