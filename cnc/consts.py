from enum import Enum


class Commands(Enum):
    OFF: bytes = b'\x40'
    ON: bytes = b'\x41'
    RUN: bytes = b'\x43'
    PAUSE: bytes = b'\x44'
    HOMING: bytes = b'\x45'
    SYNC_PROFILES: bytes = b'\x46'
