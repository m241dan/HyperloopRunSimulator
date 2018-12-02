ACCEL_TIME      = 1.0  # milliseconds
STRIPE_DISTANCE = 100  # feet


def accel_function(time):
    return (300 / 60 / 60) * 5280  # 400 mph to feet per second


def deccel_function(time):
    return 0  # for now, let's assume strong braking?
