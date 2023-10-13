import dash_bootstrap_components
from dash import html, callback, Output, Input
from dash_iconify import DashIconify

from assets.icons import ProfileIcons
from components.profile_components.consts import ProfileGrid, ProfileForm
from database.database_manager import DatabaseManager
from models.profile import Profile
from utilities import validate_arguments


def generate_profile_single_stat(profile_name: str, icons: list[DashIconify], stat_description: str, stat_value: int):
    return html.Div([
        dash_bootstrap_components.Tooltip(stat_description, target=profile_name + stat_description, placement='top'),
        html.Div(icons, style={'margin-right': '5px'}, className='flex', id=profile_name + stat_description),
        stat_value
    ], className='flex', style={'align-items': 'center', 'justify-content': 'space-between'})


def generate_profile_details(profile: Profile):
    return [
        generate_profile_single_stat(profile.name, [ProfileIcons.BREATH, ProfileIcons.RIGHT_BROKEN_ARROW],
                                     'Inspirium Time[ms]', profile.inspirium_time),
        generate_profile_single_stat(profile.name, [ProfileIcons.BREATH, ProfileIcons.HOLD], 'Inspirium Hold Time[ms]',
                                     profile.inspirium_hold_time),
        generate_profile_single_stat(profile.name, [ProfileIcons.BREATH, ProfileIcons.LEFT_BROKEN_ARROW],
                                     'Expirium Time[ms]', profile.expirium_time),
        generate_profile_single_stat(profile.name, [ProfileIcons.BREATH, ProfileIcons.HOLD], 'Expirium Hold Time[ms]',
                                     profile.expirium_hold_time),
        generate_profile_single_stat(profile.name, [ProfileIcons.LUNGS], 'Tidal Volume[liter]', profile.tidal_volume),
        generate_profile_single_stat(profile.name, [ProfileIcons.TIME], 'Profile Run Time[seconds]', profile.time_span),
    ]


def generate_profile_card(profile: Profile):
    return html.Div([
        html.Label(profile.name, className='flex-center', style={'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(className='margin full-width'),
        html.Div(generate_profile_details(profile))
    ], className='grid-card')


profiles_grid = html.Div([], className='grid', id=ProfileGrid.ID)


@callback(Output(ProfileGrid.ID, 'children'),
          Input(ProfileForm.ADD_BUTTON, 'n_clicks'))
def update_profile_list(new_profile_button: int):
    return [generate_profile_card(profile) for profile in DatabaseManager().profile_manager.profiles.values()]
