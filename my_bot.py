import asyncio
import random

from lia.bot import Bot
from lia.networking_client import connect


# This is your bot. Implement it with your logic.
#
# In this example bot keeps sending units to random locations on map
# and is able to shoot when it sees an opponent, it does not aim at
# him though!
class MyBot(Bot):

    # Called only once when the game is initialized holding data about the map.
    def process_game_environment(self, game_environment):
        # We store the map that game uses in our variable.
        # https://docs.liagame.com/api/#mapdata for the data you receive here
        self.map = game_environment["map"]

    # Repeatedly called 10 times per second from game engine with
    # game state updates. Here is where all the things happen.
    def process_game_state(self, game_state, api):

        # Iterate through the data of all of your units
        for unit in game_state["units"]:

            # navigationPath is a field of your unit that shows the path
            # on which the unit is currently using if you have sent it
            # to a location using a api.navigationStart method.
            # If it is empty it means there is no path set. In this case
            # we choose a new destination and send the unit there.
            if len(unit["navigationPath"]) == 0:
                # Generate a point on map
                x, y = self.random_valid_point_on_map()
                # Send the unit to chosen point
                api.navigation_start(unit["id"], x, y)

            # If the unit has an opponent in it's viewing area then make it shoot
            if len(unit["opponentsInView"]) > 0:
                api.shoot(unit["id"])

    # Finds a random point on the map that is not on the obstacle
    def random_valid_point_on_map(self):
        min_distance_to_map_edge = 2

        # Generate new x and y until you get one that is not placed on an obstacle
        while True:
            x = random.randint(min_distance_to_map_edge, len(self.map) - min_distance_to_map_edge)
            y = random.randint(min_distance_to_map_edge, len(self.map[0]) - min_distance_to_map_edge)
            # If map at (x,y) is False it means there is no obstacle on that field
            if self.map[x][y] is False:
                return x, y


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect(MyBot()))
