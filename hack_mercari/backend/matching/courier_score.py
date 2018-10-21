import json
from math import sqrt

import pandas as pd

from . import config


def should_courier_be_assigned(delivery, courier):
    score_1 = calculate_courier_preference_score(
        delivery.sender_preference, courier
    )
    score_2 = calculate_courier_preference_score(
        delivery.recipient_preference, courier
    )
    return min(score_1, score_2) >= config.MINIMUM_SCORE_EXPECTED


def calculate_courier_preference_score(preference, courier):
    history = pd.read_csv(f'data/history_{courier.username}.csv')
    where = json.loads(preference.where)
    return score(
        history,
        preference.when_min.weekday(),
        preference.when_min.timestamp(),
        preference.when_max.timestamp(),
        where['position']['lat'],
        where['position']['lng']
    )


def score(data, weekday, time_min, time_max, latitude, longitude, radius=config.RADIUS):
    data = data.loc[
        (data['time_of_day'] >= (time_min.hour * 60 + time_min.minute)) &
        (data['time_of_day'] <= (time_max.hour * 60 + time_max.minute)) &
        (data['weekday'] == weekday)
        ]

    def is_in_radius(row):
        distance = sqrt((row['latitude'] - latitude) ** 2 + (row['longitude'] - longitude) ** 2)
        return distance <= radius

    data['is_in_radius'] = data.apply(is_in_radius, axis=1)
    return data['is_in_radius'].value_counts(normalize=True)[True]
