from enum import Enum


class Commands(Enum):
    OFF: bytes = b'\x44'
    ON: bytes = b'\x43'
    RUN: bytes = b'\x41'
    PAUSE: bytes = b'\x42'
    HOMING: bytes = b'\x45'
    SYNC_PROFILES: bytes = b'\x46'
