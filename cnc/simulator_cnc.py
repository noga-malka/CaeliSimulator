from cnc.cnc import Cnc
from connections.demo_connection import DemoConnection


class SimulatorCnc(Cnc):
    def initiate(self):
        self.connection = DemoConnection()
