from django.db import models


class Delivery(models.Model):
    STATUS_PENDING = 1
    STATUS_IN_PROGRESS = 2
    STATUS_DONE = 3
    STATUS_CHOICES = (
        (STATUS_PENDING, 'Waiting for courier to pick-up'),
        (STATUS_IN_PROGRESS, 'Courier is on the way'),
        (STATUS_DONE, 'Package has been delivered')
    )
    sender = models.ForeignKey(
        'users.User',
        related_name='+',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        'users.User',
        related_name='+',
        on_delete=models.CASCADE
    )
    courier = models.ForeignKey(
        'users.User',
        related_name='+',
        on_delete=models.CASCADE
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES
    )
