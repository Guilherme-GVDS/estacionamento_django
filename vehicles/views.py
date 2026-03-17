from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets

from vehicles.filters import VehicleFilter, VehicleTypeFilter
from .models import VehicleType, Vehicle
from .serializers import VehicleSerializer, VehicleTypeSerializer
from core.permissions import IsOwner


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwner]
    rql_filter_class = VehicleFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    rql_filter_class = VehicleTypeFilter
