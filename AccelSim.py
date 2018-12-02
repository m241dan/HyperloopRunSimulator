from AccelSimConfig import *


class AccelSim:
    def __init__(self, initial_time):
        self.position = 0.0
        self.velocity = 0.0
        self.acceleration = 0.0
        self.prev_time = initial_time
        self.run_time = 0.0
        return

    def update(self, time):
        time_dif = time - self.prev_time
        self.run_time += time_dif

        if self.run_time < ACCEL_TIME:
            self.acceleration = accel_function(self.run_time)
        else:
            self.acceleration = deccel_function(self.run_time)

        self.velocity += self.acceleration * time_dif  # integrating
        self.position += self.velocity  # integrating

        self.prev_time = time
        return

    def get_stripe_count(self):
        return int(self.position / STRIPE_DISTANCE)
