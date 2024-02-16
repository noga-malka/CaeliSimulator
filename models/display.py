from dataclasses import dataclass


@dataclass
class DisplayCard:
    card_id: str
    title: str
    size: str
    display_type: str
    inputs: list[str]
    typing: str
