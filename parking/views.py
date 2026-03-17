from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets

from parking.filters import ParkingRecordFilter, ParkingSpotFilter
from .models import ParkingRecord, ParkingSpot
from .serializers import ParkingRecordSerializer, ParkingSpotSerializer
from core.permissions import IsOwner


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]
    rql_filter_class = ParkingSpotFilter


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwner]
    rql_filter_class = ParkingRecordFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)
