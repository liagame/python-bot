from enum import Enum


class Api:
    def __init__(self, uid):
        self.response = {}
        self.uid = uid
        self.type = "RESPONSE"
        self.thrustSpeedEvents = []
        self.rotationEvents = []
        self.shootEvents = []

    def set_thrust_speed(self, unit_id, speed):
        self.thrustSpeedEvents.append({"unitId": unit_id, "speed": speed.name})

    def set_rotation_speed(self, unit_id, rotation):
        self.rotationEvents.append({"unitId": unit_id, "rotation": rotation.name})

    def shoot(self, unit_id):
        self.shootEvents.append({"unitId": unit_id})


class ThrustSpeed(Enum):
    NONE = 1
    FORWARD = 2
    BACKWARD = 3


class Rotation(Enum):
    NONE = 1
    LEFT = 2
    RIGHT = 3
