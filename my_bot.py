import asyncio
import random

from lia.bot import Bot
from lia.networking_client import connect


# Here is where you control your bot. Initial implementation keeps sending units
# to random locations on the map and makes them shoot when they see opponents.
class MyBot(Bot):

    # In this method we receive the basic information about the game environment.
    # - GameEnvironment reference: TODO link
    def process_game_environment(self, game_environment):

        # Here we store the map as a 2D array of booleans. If map[x][y] equals True that
        # means that at (x,y) there is an obstacle. x=0, y=0 points to bottom left corner.
        self.map = game_environment["map"]

    # This is the main method where you control your bot. 10 times per game second it
    # receives current game state. Use Api object to call actions on your units.
    # - GameState reference: TODO link
    # - Api reference:       TODO link
    def process_game_state(self, game_state, api):

        # We iterate through all of our units that are still alive.
        for unit in game_state["units"]:

            # If the unit is not going anywhere, we choose a new valid point on the
            # map and send the unit there.
            if len(unit["navigationPath"]) == 0:

                x = None
                y = None

                # Generate new x and y until you get a position on the map where there
                # is no obstacle.
                while True:
                    x = random.randint(0, len(self.map) - 1)
                    y = random.randint(0, len(self.map[0]) - 1)
                    # False means that on (x,y) there is no obstacle.
                    if self.map[x][y] is False:
                        break

                # Make the unit go to the chosen x and y.
                api.navigation_start(unit["id"], x, y)

            # If the unit sees an opponent then make it shoot.
            if len(unit["opponentsInView"]) > 0:
                api.shoot(unit["id"])

                # Don't forget to make your unit brag. :)
                api.say_something(unit["id"], "I see you!")


# Connects your bot to Lia game engine, don't change it.
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect(MyBot()))
