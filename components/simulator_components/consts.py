from assets.icons import ControlButtonIcons


class ConnectionStatus:
    ID = 'connection_status_bar'


class ButtonIds:
    CONNECT_TO_SIMULATOR = 'connect_to_simulator_modal'
    DISCONNECT_FROM_SIMULATOR = 'disconnect_connection_button'

    class Simulator:
        ON = 'simulator_on'
        RUN = 'simulator_run'
        HOMING = 'simulator_homing'
        STOP = 'simulator_emergency_stop'
        OFF = 'simulator_off'

        class PauseResume:
            ID = 'simulator_pause_resume'
            PAUSE_BUTTON = [ControlButtonIcons.PAUSE, 'Pause']
            RESUME_BUTTON = [ControlButtonIcons.RESUME, 'Resume']


class ButtonGroupIds:
    SETUP_SIMULATOR = 'setup_simulator'
    SIMULATOR_CONTROLS = 'simulator_controls'


class ConnectionModal:
    ID = 'connection_modal'
    CONNECTION_TYPE_DROPDOWN = 'connection_type_dropdown'
    DEVICE_DROPDOWN = 'device_dropdown'
    SYNC_DEVICES = 'sync_devices'
    CONNECT_DEVICE = 'connect_device'


class SelectTestCaseModal:
    ID = 'select_test_case_modal'
    SEND_TEST_CASE = 'send_test_case'
    TEST_CASE_DROPDOWN = 'test_case_dropdown'


class LiveData:
    ID = 'live_data_container'
    INTERVAL = 'live_data_interval'
