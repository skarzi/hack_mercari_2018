from rest_framework.permissions import BasePermission


class AnonymousOnly(BasePermission):
    def has_permission(self, request, view):
        return not request.user or not request.user.is_authenticated


class CourierOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_courier
