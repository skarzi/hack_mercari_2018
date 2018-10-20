from rest_framework.routers import DefaultRouter

from deliveries.api import DeliveriesViewSet
from users.api import AuthViewSet

api_router = DefaultRouter()
api_router.register('auth', AuthViewSet, base_name='auth')
api_router.register('deliveries', DeliveriesViewSet, base_name='deliveries')
