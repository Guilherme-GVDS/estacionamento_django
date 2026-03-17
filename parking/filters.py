from dj_rql.filter_cls import AutoRQLFilterClass

from .models import ParkingRecord, ParkingSpot


class ParkingSpotFilter(AutoRQLFilterClass):
    MODEL = ParkingSpot


class ParkingRecordFilter(AutoRQLFilterClass):
    MODEL = ParkingRecord
    FILTERS = (
        {
            'filter': 'license_plate',
            'source': 'vehicle__license_plate',
        },
    )
