class ConnectionStatus:
    ID = 'connection_status_bar'


class ButtonIds:
    CONNECT_TO_SIMULATOR = 'connect_to_simulator_modal'
    DISCONNECT_FROM_SIMULATOR = 'disconnect_connection_button'
    TEST_CASE = 'select_test_case_modal'

    class Simulator:
        ON = 'simulator_on'
        RUN = 'simulator_run'
        HOMING = 'simulator_homing'
        PAUSE = 'simulator_pause'
        OFF = 'simulator_off'


class ButtonGroupIds:
    SETUP_SIMULATOR = 'setup_simulator'
    SIMULATOR_CONTROLS = 'simulator_controls'


class ConnectionModal:
    ID = 'connection_modal'
    CONNECTION_TYPE_DROPDOWN = 'connection_type_dropdown'
    DEVICE_DROPDOWN = 'device_dropdown'
    SYNC_DEVICES = 'sync_devices'
    CONNECT_DEVICE = 'connect_device'
