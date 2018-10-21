from config.celery import app
from matching.courier_score import should_courier_be_assigned
from services.pusher import PusherClient


@app.task()
def assign_couriers(delivery_id):
    #  prevent recursive import
    from deliveries.models import Delivery
    from assignments.models import CourierAssignmentProposition
    from users.models import User

    delivery = Delivery.objects.get(id=delivery_id)
    couriers = User.objects.filter(is_courier=True)
    for courier in couriers.all():
        if should_courier_be_assigned(delivery, courier):
            CourierAssignmentProposition.objects.create(
                courier=courier, delivery=delivery
            )
            PusherClient.trigger(
                [courier.username],
                'new-assignment', {}
            )
            print(f"Courier {courier.username} assigned!")
