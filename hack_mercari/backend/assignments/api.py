from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from assignments.models import CourierAssignmentProposition
from assignments.serializers import CourierAssignmentPropositionSerializer
from deliveries.models import Delivery
from deliveries.serializers import DeliverySerializer
from users.permissions import CourierOnly


class CourierAssignmentPropositionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, CourierOnly)
    serializer_class = CourierAssignmentPropositionSerializer

    def get_queryset(self):
        return CourierAssignmentProposition.objects.filter(
            courier=self.request.user
        )

    def retrieve(self, request, *args, **kwargs):
        # terrible workaround
        delivery = Delivery.objects.get(pk=kwargs.get("pk"))
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().select_related('delivery')
        serializer = DeliverySerializer(
            [assignment.delivery for assignment in qs], many=True
        )
        return Response(serializer.data)

    @action(methods=["POST"], detail=True)
    def accept(self, request, *args, **kwargs):
        delivery = Delivery.objects.get(pk=kwargs.get("pk"))
        courier = request.user

        delivery.courier = courier
        delivery.status = delivery.STATUS_WAITING_FOR_COURIER
        delivery.save()
        CourierAssignmentProposition.objects.filter(
            delivery=delivery
        ).delete()
        return Response()
