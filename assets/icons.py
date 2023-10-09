from dash_iconify import DashIconify


def create_icon(icon: str, width: int, **kwargs):
    return DashIconify(icon=icon, width=width, **kwargs)


class SmallIcons:
    RIGHT_ARROW = create_icon('basil:arrow-right-solid', width=25)
    DOWN_ARROW = create_icon('basil:arrow-down-solid', width=25)


class MediumIcons:
    BREATH = create_icon('openmoji:wind-face', width=32)
    RIGHT_BROKEN_ARROW = create_icon('solar:arrow-right-broken', width=32)
    LEFT_BROKEN_ARROW = create_icon('solar:arrow-left-broken', width=32)
    HOLD = create_icon('bi:pause', width=32)
    LUNGS = create_icon('healthicons:lungs-outline', width=32)
    TIME = create_icon('carbon:time', width=32)


class BigIcons:
    BLUETOOTH = create_icon('ic:round-bluetooth', width=45, style={'margin-right': '8px'})
    SERIAL = create_icon('ph:usb-fill', width=45, style={'margin-right': '8px'})
    MANAGE_PROFILES = create_icon('carbon:user-profile', width=45, style={'margin-right': '8px'})
    MANAGE_TEST_CASES = create_icon('fluent-mdl2:test-case', width=45, style={'margin-right': '8px'})
    RUN_SIMULATOR = create_icon('carbon:play-filled', width=45, style={'margin-right': '8px'})
