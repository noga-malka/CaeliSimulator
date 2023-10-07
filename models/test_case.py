from dataclasses import dataclass


@dataclass
class TestCase:
    name: str
    profile_names: list[str]
