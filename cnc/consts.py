from enum import Enum


class Connections:
    BLUETOOTH = 'Bluetooth'
    SERIAL = 'Serial'
    DEMO = 'Demo'


class ProtocolConsts:
    HEADER = bytes.fromhex('aa55aa')
    FOOTER = bytes.fromhex('0000')
    SEPARATOR = '\t'


class Commands(Enum):
    RUN: bytes = b'\x41'
    STOP: bytes = b'\x42'
    ON: bytes = b'\x43'
    OFF: bytes = b'\x44'
    HOMING: bytes = b'\x45'
    SEND_TEST_CASE: bytes = b'\x46'
    PAUSE_SESSION: bytes = b'\x47'
    RESUME_SESSION: bytes = b'\x48'
    SET_BLOWER_1_SPEED: bytes = b'\x31'
    SET_BLOWER_2_SPEED: bytes = b'\x32'
    CALIBRATE: bytes = b'\x24'
