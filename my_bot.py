from lia.callable import Bot
from lia.networking_client import NetworkingClient
from lia.api import *
import random


class MyBot(Bot):

    def __init__(self):
        self.count = 0
        self.should_shoot = True
        random.seed = 1

    def process_map_data(self, map_data):
        print(map_data)

    def process_state(self, state_update, api):
        for unit in state_update['units']:
            id = unit['id']

            if self.count % 10 == 0 or self.count % 11 == 0:
                # Rotation
                rand = random.random()
                if rand < 0.4:
                    api.set_rotation_speed(id, Rotation.LEFT)
                elif rand < 0.9:
                    api.set_rotation_speed(id, Rotation.RIGHT)
                else:
                    api.set_rotation_speed(id, Rotation.NONE)

                # Thrust speed
                rand = random.random()
                if rand < 0.8:
                    api.set_thrust_speed(id, ThrustSpeed.FORWARD)
                elif rand < 0.9:
                    api.set_thrust_speed(id, ThrustSpeed.BACKWARD)
                else:
                    api.set_thrust_speed(id, ThrustSpeed.NONE)

            # Shoot all three bullets when they are loaded
            if unit['nBullets'] == 3:
                self.should_shoot = True
            elif unit['nBullets'] == 0:
                self.should_shoot = False

            if unit['canShoot'] and self.should_shoot:
                api.shoot(id)

            self.count += 1


if __name__ == "__main__":
    client = NetworkingClient(MyBot())
    client.connect()
