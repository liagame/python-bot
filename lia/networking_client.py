import ssl
import traceback

import websocket
import json
from lia.api import Api

try:
    import thread
except ImportError:
    import _thread as thread


class NetworkingClient:

    def __init__(self, bot):
        self.bot = bot
        self.ws = websocket.WebSocketApp("ws://localhost:8887",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open)

    def connect(self):
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE,
                               "check_hostname": False})

    def on_message(self, ws, message):
        data = json.loads(message)

        response = Api(data['uid'])
        try:
            if data['type'] == 'MAP_DATA':
                self.bot.process_map_data(data)

            elif data['type'] == 'STATE_UPDATE':
                self.bot.process_state(data, response)

            ws.send(json.dumps(response.__dict__))

        except Exception as e:
            traceback.print_exc()

    def on_error(self, ws, error):
        traceback.print_exc()
        exit(1)

    def on_close(self, ws):
        print("Connection closed. Exiting...")

    def on_open(self, ws):
        print("Connected!")

