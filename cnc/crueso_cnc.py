from cnc.cnc import Cnc
from singleton import Singleton


class CruesoCnc(Cnc, Singleton):
    def initiate(self):
        super(CruesoCnc, self).initiate()
