from django.db import models


class CourierAssignmentProposition(models.Model):
    delivery = models.ForeignKey(
        'deliveries.Delivery',
        on_delete=models.CASCADE
    )
    courier = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
