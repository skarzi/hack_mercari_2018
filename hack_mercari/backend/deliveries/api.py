from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from deliveries.models import Delivery
from deliveries.serializers import CreateDeliverySerializer, DeliverySerializer


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
