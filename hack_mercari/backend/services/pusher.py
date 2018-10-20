import pusher
from django.conf import settings


def get_pusher_client():
    return pusher.Pusher(
        app_id=settings.PUSHER_APP_ID,
        key=settings.PUSHER_KEY,
        secret=settings.PUSHER_SECRET,
        cluster=settings.PUSHER_CLUSTER,
        ssl=True
    )


PusherClient = get_pusher_client()
