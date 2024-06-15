from dash_iconify import DashIconify


def create_icon(icon: str, width: int, **kwargs):
    return DashIconify(icon=icon, width=width, **kwargs)


class TestCaseIcons:
    RIGHT_ARROW = create_icon('basil:arrow-right-solid', width=25)
    DOWN_ARROW = create_icon('basil:arrow-down-solid', width=25)


class ProfileIcons:
    BREATH = create_icon('openmoji:wind-face', width=32)
    RIGHT_BROKEN_ARROW = create_icon('solar:arrow-right-broken', width=32)
    LEFT_BROKEN_ARROW = create_icon('solar:arrow-left-broken', width=32)
    HOLD = create_icon('bi:pause', width=32)
    LUNGS = create_icon('healthicons:lungs-outline', width=32)
    TIME = create_icon('carbon:time', width=32)


class ControlButtonIcons:
    CONNECT_TO_SIMULATOR = create_icon('wpf:connected', width=32, style={'marginRight': '3px'})
    DISCONNECT_FROM_SIMULATOR = create_icon('wpf:disconnected', width=32, style={'marginRight': '3px'})
    SELECT_TEST_CASE = create_icon('fluent-mdl2:test-case', width=32, style={'marginRight': '3px'})
    CALIBRATE = create_icon('mynaui:config', width=32, style={'marginRight': '3px'})
    ON = create_icon('iconoir:on-tag', width=32, style={'marginRight': '3px'})
    RUN = create_icon('carbon:play-filled', width=32, style={'marginRight': '3px'})
    HOMING = create_icon('ant-design:home-filled', width=32, style={'marginRight': '3px'})
    STOP = create_icon('bi:stop-fill', width=32, style={'marginRight': '3px'})
    PAUSE = create_icon('ic:round-pause', width=32, style={'marginRight': '3px'})
    RESUME = create_icon('material-symbols:resume-rounded', width=32, style={'marginRight': '3px'})
    OFF = create_icon('iconoir:off-tag', width=32, style={'marginRight': '3px'})
    CLOSE = create_icon('ic:round-close', width=32)


class NavigationBarIcons:
    PROFILE_MANAGER = create_icon('carbon:user-profile', width=45, style={'marginRight': '8px'})
    TEST_CASE_MANAGER = create_icon('fluent-mdl2:test-case', width=45, style={'marginRight': '8px'})
    RUN_SIMULATOR = create_icon('carbon:play-filled', width=45, style={'marginRight': '8px'})
