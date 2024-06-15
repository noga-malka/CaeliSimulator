from dataclasses import dataclass


@dataclass
class DisplayCard:
    card_id: str
    title: str
    size: str
    display_type: str
    length_in_minutes: float
    inputs: list[str]
    typing: str
