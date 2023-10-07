from dataclasses import dataclass
from profile import Profile


@dataclass
class TestCase:
    name: str
    profiles: list[Profile]
