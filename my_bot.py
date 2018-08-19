from lia.callable import Bot
from lia.networking_client import NetworkingClient
from lia.api import *


class MyBot(Bot):
    
    def process_map_data(self, map_data):
        print(map_data)

    def process_state(self, state_update, api):
        print(state_update)

if __name__ == "__main__":
    client = NetworkingClient(MyBot())
    client.connect()
