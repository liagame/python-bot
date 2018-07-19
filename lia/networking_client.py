import ssl
import traceback
import argparse
import websocket
import json
from lia.api import Api


try:
    import thread
except ImportError:
    import _thread as thread


class NetworkingClient:

    def __init__(self, bot):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--port", help="specify port", required=False)
        parser.add_argument("-i", "--id", help="unique identifier", required=False)
        args = parser.parse_args()

        if args.port is None: args.port = "8887"
        if args.id is None: args.id = ""

        self.bot = bot
        self.ws = websocket.WebSocketApp("ws://localhost:" + args.port,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open,
                                         header={'Id': args.id})

        self.finished = False

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
        if not self.finished:
            traceback.print_exc()
            exit(1)

    def on_close(self, ws):
        print("Connection closed. Exiting...")
        self.finished = True
        exit(0)


    def on_open(self, ws):
        print("Connected!")

