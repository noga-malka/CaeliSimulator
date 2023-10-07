from dataclasses import dataclass


@dataclass
class Profile:
    name: str
    inspirium_time: int
    inspirium_hold_time: int
    expirium_time: int
    expirium_hold_time: int
    tidal_volume: int
    time_span: int
