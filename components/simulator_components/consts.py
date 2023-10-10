class Connection:
    STATUS_BAR = 'connection_status_bar'


class ButtonIds:
    BLUETOOTH = 'open_bluetooth_modal'
    SERIAL = 'open_serial_modal'
    TEST_CASE = 'open_test_case_modal'

    class Simulator:
        ON = 'simulator_on'
        RUN = 'simulator_run'
        HOMING = 'simulator_homing'
        PAUSE = 'simulator_pause'
        OFF = 'simulator_off'


class ButtonGroupIds:
    SETUP_SIMULATOR = 'setup_simulator'
    SIMULATOR_CONTROLS = 'simulator_controls'


class BluetoothModal:
    ID = 'bluetooth_modal'
    DEVICE_DROPDOWN = 'bluetooth_device_dropdown'
    SYNC_DEVICES = 'sync_bluetooth_devices'
    CONNECT_DEVICE = 'connect_bluetooth_device'
