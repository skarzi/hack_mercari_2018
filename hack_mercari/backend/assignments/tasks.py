from config.celery import app


@app.task()
def assign_couriers(delivery_id):
    #  prevent recursive import
    from deliveries.models import Delivery
    from assignments.models import CourierAssignmentProposition
    from users.models import User

    delivery = Delivery.objects.get(id=delivery_id)
    couriers = User.objects.filter(is_courier=True)
    for courier in couriers.all():
        CourierAssignmentProposition.objects.create(
            courier=courier, delivery=delivery
        )

    # todo: this should use actual ML algorithm
