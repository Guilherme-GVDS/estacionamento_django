from rest_framework import viewsets
from .models import ParkingRecord, ParkingSpot
from .serializers import ParkingRecordSerializer, ParkingSpotSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer


class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
