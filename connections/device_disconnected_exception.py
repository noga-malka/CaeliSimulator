class DeviceDisconnectedException(Exception):
    def __init__(self, device_type: str):
        self.message = f'Device {device_type} disconnected. Connection closed'

    def __str__(self):
        return self.message
