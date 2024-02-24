from assets.icons import ControlButtonIcons


class ConnectionStatus:
    ID = 'connection_status_bar'


class ButtonIds:
    class Crueso:
        FIRST_BLOWER_SPEED_VALUE = 'first_blower_speed_value'
        SECOND_BLOWER_SPEED_VALUE = 'second_blower_speed_value'

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


class SelectTestCaseModal:
    ID = 'select_test_case_modal'
    SEND_TEST_CASE = 'send_test_case'
    TEST_CASE_DROPDOWN = 'test_case_dropdown'


class LiveData:
    INTERVAL = 'live_data_interval'


class ProgressBar:
    ID = 'progress_bar'
    STEPS = 'progress_steps'
    STEP_PERCENTAGE_WIDTH = 8
    CURRENT_TEST_CASE = 'current_test_case'
