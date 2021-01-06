from tcpcom import TCPServer
import time


class ReactiveSocketServer(object):

    def __init__(self, carrier):
        self.host = "127.0.0.1"
        self.port = 4353  # XCSoar Open Vario Port.
        self.data_carrier = carrier
        self.server = TCPServer(port=self.port, stateChanged=self.on_state_change)

    def on_state_change(self, state, msg):

        if state == "LISTENING":
            print("Data stream available")
        elif state == "CONNECTED":
            print(f"Client connected to {msg}. Begin sensor data transmission.")
            while True:
                self.server.sendMessage(self.data_carrier)
        elif state == "MESSAGE":
            print(f"Message received: {msg}")
