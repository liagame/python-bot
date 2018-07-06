from enum import Enum


class Api:
    def __init__(self, uid):
        self.response = {}
        self.uid = uid
        self.type = "RESPONSE"
        self.thrustSpeedEvents = []
        self.rotationEvents = []
        self.shootEvents = []

    def set_thrust_speed(self, player_id, speed):
        self.thrustSpeedEvents.append({"playerId": player_id, "speed": speed.name})

    def set_rotation_speed(self, player_id, rotation):
        self.rotationEvents.append({"playerId": player_id, "rotation": rotation.name})

    def shoot(self, player_id):
        self.shootEvents.append({"playerId": player_id})


class ThrustSpeed(Enum):
    NONE = 1
    FORWARD = 2
    BACKWARD = 3


class Rotation(Enum):
    NONE = 1
    LEFT = 2
    RIGHT = 3
