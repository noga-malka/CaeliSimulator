from enum import Enum


class Commands(Enum):
    OFF: bytes = b'\x44'
    ON: bytes = b'\x43'
    RUN: bytes = b'\x41'
    STOP: bytes = b'\x42'
    HOMING: bytes = b'\x45'
    SEND_TEST_CASE: bytes = b'\x46'
    PAUSE_SESSION: bytes = b'\x47'
    RESUME_SESSION: bytes = b'\x48'
