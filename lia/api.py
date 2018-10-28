from enum import Enum


class Api:
    def __init__(self, uid):
        self.response = {}
        self.uid = uid
        self.current_index = 0
        self.type = "RESPONSE"
        self.speedEvents = []
        self.rotationEvents = []
        self.shootEvents = []
        self.navigationStartEvents = []
        self.navigationStopEvents = []

    def get_index(self):
        index = self.current_index
        self.current_index += 1
        return index

    def set_speed(self, unit_id, speed):
        self.speedEvents.append({"index": self.get_index(), "unitId": unit_id, "speed": speed.name})

    def set_rotation(self, unit_id, rotation):
        self.rotationEvents.append({"index": self.get_index(), "unitId": unit_id, "rotation": rotation.name})

    def shoot(self, unit_id):
        self.shootEvents.append({"index": self.get_index(), "unitId": unit_id})

    def navigation_start(self, unit_id, x, y):
        self.navigationStartEvents.append({"index": self.get_index(), "unitId": unit_id, "x": x, "y": y})

    def navigation_stop(self, unit_id):
        self.navigationStopEvents.append({"index": self.get_index(), "unitId": unit_id})


class Speed(Enum):
    NONE = 1
    FORWARD = 2
    BACKWARD = 3


class Rotation(Enum):
    NONE = 1
    LEFT = 2
    SLOW_LEFT = 3
    RIGHT = 4
    SLOW_RIGHT = 5
