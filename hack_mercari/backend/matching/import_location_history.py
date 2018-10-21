import json
from datetime import datetime

import pandas as pd

from . import config


def import_location_history(courier, filename):
    # load data
    with open(filename, "r") as f:
        data = json.load(f)['locations']
    df = pd.DataFrame(data)[['latitudeE7', 'longitudeE7', 'timestampMs']]

    # transform columns values
    df[['timestamp']] = df[['timestampMs']].apply(lambda x: pd.to_numeric(x) // 10e2)
    df[['latitude']] = df[['latitudeE7']].apply(lambda x: x / 10e6)
    df[['longitude']] = df[['longitudeE7']].apply(lambda x: x / 10e6)
    df = df.drop(columns=['timestampMs', 'latitudeE7', 'longitudeE7'])

    # filter by location boundaries
    LAT_MIN, LAT_MAX = config.LAT_BOUNDARIES
    LNG_MIN, LNG_MAX = config.LNG_BOUNDARIES
    df = df.loc[(df['latitude'] >= LAT_MIN) & (df['latitude'] <= LAT_MAX)]
    df = df.loc[(df['longitude'] >= LNG_MIN) & (df['longitude'] <= LNG_MAX)]

    # filter by time boundaries
    TIME_MIN, TIME_MAX = config.TIME_BOUNDARIES
    df = df.loc[(df['timestamp'] >= TIME_MIN.timestamp()) & (df['timestamp'] <= TIME_MAX.timestamp())]

    # weekday
    def get_weekday(row):
        dt = datetime.utcfromtimestamp(row['timestamp'])
        return dt.weekday()

    df['weekday'] = df.apply(lambda row: get_weekday(row), axis=1)

    # time of day
    def get_time_of_day(row):
        dt = datetime.utcfromtimestamp(row['timestamp'])
        return (dt.hour * 60 + dt.minute)

    df['time_of_day'] = df.apply(lambda row: get_time_of_day(row), axis=1)

    # filter by time of day
    TOD_MIN, TOD_MAX = config.TIME_OF_DAY_BOUNDARIES
    df = df.loc[
        (df['time_of_day'] >= (TOD_MIN.hour * 60 + TOD_MIN.minute)) &
        (df['time_of_day'] <= (TOD_MAX.hour * 60 + TOD_MAX.minute))
        ]

    # save to csv
    df.to_csv(f'data/history_{courier.username}.csv', index=False)
