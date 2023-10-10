import sys

from cnc.consts import Commands
from cnc.packets.base_packet import BasePacket
from database.database_manager import DatabaseManager
from models.profile import Profile
from models.test_case import TestCase


class SyncTestCasePacket(BasePacket):
    def __init__(self, command_type: Commands, test_case: TestCase):
        super().__init__(command_type)
        self.test_case = test_case

    def build_payload(self):
        profile_number = len(self.test_case.profile_names).to_bytes(2, sys.byteorder)
        database = DatabaseManager()
        profiles = b''
        for profile_name in self.test_case.profile_names:
            profiles += self._profile_to_bytes(database.profile_manager.profiles[profile_name])
        return profile_number + profiles

    @staticmethod
    def _profile_to_bytes(profile: Profile):
        ordered_details = [
            profile.inspirium_time,
            profile.inspirium_hold_time,
            profile.expirium_time,
            profile.expirium_hold_time,
            profile.tidal_volume * 1000,  # convert liter to milliliter
            profile.time_span
        ]
        return b''.join([detail.to_bytes(2, sys.byteorder) for detail in ordered_details])
