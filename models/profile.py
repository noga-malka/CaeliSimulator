from dataclasses import dataclass


@dataclass
class Profile:
    profile_name: str
    inspirium_input: int
    inspirium_hold_input: int
    expirium_input: int
    expirium_hold_input: int
    tidal_volume: int
    time_span: int
