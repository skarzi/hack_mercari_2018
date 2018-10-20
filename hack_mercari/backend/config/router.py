from rest_framework.routers import DefaultRouter

from users.api import AuthViewSet

api_router = DefaultRouter()
api_router.register('auth', AuthViewSet, base_name='auth')
