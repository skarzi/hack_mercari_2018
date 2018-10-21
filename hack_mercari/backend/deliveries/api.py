from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from assignments.tasks import assign_couriers
from deliveries.models import Delivery
from deliveries.serializers import CreateDeliverySerializer, DeliverySerializer
from preferences.serializers import MeetingPreferenceSerializer
from services.pusher import PusherClient


class DeliveriesViewSet(ModelViewSet):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_courier:
            qs = Delivery.objects.filter(courier=user)
        else:
            qs = Delivery.objects.filter(
                Q(sender=user) | Q(recipient=user)
            )
        return qs.distinct()

    def create(self, request, *args, **kwargs):
        serializer = CreateDeliverySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.update({
            "sender": request.user
        })
        delivery = serializer.save()
        return Response(DeliverySerializer(delivery).data)

    @action(methods=["POST"], detail=True)
    def recipient_preference(self, request, *args, **kwargs):
        serializer = MeetingPreferenceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        delivery = self.get_object()
        delivery.recipient_preference = serializer.save()
        delivery.status = delivery.STATUS_ASSIGNING
        delivery.save()
        assign_couriers(delivery.id)
        return Response(DeliverySerializer(delivery).data)

    @action(methods=["POST"], detail=True)
    def request_pass_to_courier(self, request, *args, **kwargs):
        delivery = self.get_object()
        if request.user != delivery.courier:
            raise PermissionDenied("You're not a courier")
        PusherClient.trigger(
            [delivery.sender.username],
            'pass-to-courier', {'delivery': delivery.id}
        )
        return Response()

    @action(methods=["POST"], detail=True)
    def pass_to_courier(self, request, *args, **kwargs):
        delivery = self.get_object()
        if request.user != delivery.sender:
            raise PermissionDenied("You're not delivery sender")
        if delivery.status != Delivery.STATUS_WAITING_FOR_COURIER:
            raise PermissionDenied("Invalid delivery state")
        delivery.status = Delivery.STATUS_IN_TRANSIT
        delivery.save()
        return Response()

    @action(methods=["POST"], detail=True)
    def request_receive(self, request, *args, **kwargs):
        delivery = self.get_object()
        if request.user != delivery.courier:
            raise PermissionDenied("You're not a courier")
        PusherClient.trigger(
            [delivery.recipient.username],
            'receive', {'delivery': delivery.id}
        )
        return Response()

    @action(methods=["POST"], detail=True)
    def receive(self, request, *args, **kwargs):
        delivery = self.get_object()
        if request.user != delivery.recipient:
            raise PermissionDenied("You're not delivery recipient")
        if delivery.status != Delivery.STATUS_IN_TRANSIT:
            raise PermissionDenied("Invalid delivery state")
        delivery.status = Delivery.STATUS_DELIVERED
        delivery.save()
        return Response()
