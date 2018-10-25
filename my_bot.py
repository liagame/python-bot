import asyncio

from lia.callable import Bot
from lia.networking_client import connect
from lia.api import *


class MyBot(Bot):
    
    def process_map_data(self, map_data):
        print(map_data)

    def process_state(self, state_update, api):
        for unit in state_update["units"]:
            api.shoot(unit["id"])


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect(MyBot()))

