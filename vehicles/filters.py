from dj_rql.filter_cls import AutoRQLFilterClass

from .models import Vehicle, VehicleType


class VehicleFilter(AutoRQLFilterClass):
    MODEL = Vehicle


class VehicleTypeFilter(AutoRQLFilterClass):
    MODEL = VehicleType
