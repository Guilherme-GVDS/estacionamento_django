from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ColorViewSet,
    ModelViewSet,
    VehicleViewSet,
    VehicleTypeViewSet,
    BrandViewSet
)

router = DefaultRouter()
router.register('vehicles', VehicleViewSet)
router.register('vehicles/types', VehicleTypeViewSet)
router.register('vehicles/brands', BrandViewSet)
router.register('vehicles/models', ModelViewSet)
router.register('vehicles/colors', ColorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
