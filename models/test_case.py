from dataclasses import dataclass

from models.profile import Profile


@dataclass
class TestCase:
    name: str
    profiles: list[Profile]
