import asyncio
import random

from lia.bot import Bot
from lia.networking_client import connect


# This is your bot that will play the game for you.
#
# Implementation below keeps sending units to random locations on the map
# and makes them shoot when they see opponents.
class MyBot(Bot):

    # This method is called only once at the beginning of the game and holds the basic
    # information about the game environment.
    # - GameEnvironment reference: TODO link
    def process_game_environment(self, game_environment):

        # Here we will store the map that the game will be played on. Map has values set
        # to True where there is an obstacle. You can access (x,y) coordinate by calling
        # map[x][y] and x=0, y=0 is placed at the bottom left corner.
        self.map = game_environment["map"]

    # This method is the main part of your bot. It is called 10 times per game seconds and
    # it holds game's current state and the Api object which you use to control your units.
    # - GameState reference: TODO link
    # - Api reference:       TODO link
    def process_game_state(self, game_state, api):

        # First we iterate through all of our units that are still alive.
        for unit in game_state["units"]:

            # With api.navigationStart(...) method you can send your units to go to a
            # specified point on the map all by themselves. If they are currently going
            # somewhere then their path is stored in navigationPath field. If the field
            # is empty the unit is not going anywhere automatically. Here, if the unit
            # is not going anywhere we choose a new location and send it there.
            if len(unit["navigationPath"]) == 0:
                # Generate a point on the map where there is no obstacle.
                x, y = self.random_valid_point_on_map()
                # Make the unit go to the chosen x (point[0]) and y (point[1]).
                api.navigation_start(unit["id"], x, y)

            # If the unit sees an opponent then make it shoot.
            if len(unit["opponentsInView"]) > 0:
                api.shoot(unit["id"])

    # Finds a random point on the map where there is no obstacle.
    def random_valid_point_on_map(self):
        # Generate new x and y until you get a position that is not placed on an obstacle.
        while True:
            x = random.randint(0, len(self.map) - 1)
            y = random.randint(0, len(self.map[0]) - 1)
            # False means that on (x,y) there is no obstacle.
            if self.map[x][y] is False:
                return x, y


# This connects your bot to Lia game engine, don't change it.
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect(MyBot()))
