from rest_framework import serializers

from assignments.models import CourierAssignmentProposition
from deliveries.serializers import DeliverySerializer


class CourierAssignmentPropositionSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer()

    class Meta:
        model = CourierAssignmentProposition
        fields = ('delivery', 'courier')
