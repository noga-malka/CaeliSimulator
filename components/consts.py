class ProfileForm:
    ID = 'add_profile_form'
    ADD_BUTTON = 'add_profile_button'
    CREATE_NEW_BUTTON = 'create_new_profile_button'

    class Inputs:
        PROFILE_NAME = 'profile_name'
        INSPIRIUM_TIME = 'inspirium_input'
        INSPIRIUM_HOLD_TIME = 'inspirium_hold_input'
        EXPIRIUM_TIME = 'expirium_input'
        EXSPIRIUM_HOLD_TIME = 'expirium_hold_input'
        TIDAL_VOLUME = 'tidal_volume'
        TIME_SPAN = 'time_span'


class Placeholder:
    ID = 'placeholder'


class ProfileGrid:
    ID = 'profile_grid'


class TestCaseGrid:
    ID = 'test_case_grid'


class TestCaseForm:
    ID = 'test_case_form'
    ADD_BUTTON = 'add_button'
    SELECTED_PROFILES = 'selected_profiles'

    class Inputs:
        TEST_CASE_NAME = 'test_case_name'
        PROFILE_LIST = 'profile_list'
