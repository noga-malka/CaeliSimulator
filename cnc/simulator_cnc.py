from cnc.cnc import Cnc
from singleton import Singleton


class SimulatorCnc(Cnc, Singleton):
    def initiate(self):
        super(SimulatorCnc, self).initiate()
