import dash_bootstrap_components
from dash import html, callback, Output, Input
from dash_iconify import DashIconify

from assets.icons import MediumIcons
from components.profile_components.consts import ProfileGrid, ProfileForm
from database.database_manager import DatabaseManager
from models.profile import Profile


def generate_profile_single_stat(profile_name: str, icons: list[DashIconify], stat_description: str, stat_value: int):
    return html.Div([
        dash_bootstrap_components.Tooltip(stat_description, target=profile_name + stat_description, placement='top'),
        html.Div(icons, style={'margin-right': '5px'}, className='flex', id=profile_name + stat_description),
        stat_value
    ], className='flex', style={'align-items': 'center', 'justify-content': 'space-between'})


def generate_profile_details(profile: Profile):
    return [
        generate_profile_single_stat(profile.name, [MediumIcons.BREATH, MediumIcons.RIGHT_BROKEN_ARROW],
                                     'Inspirium Time[ms]', profile.inspirium_time),
        generate_profile_single_stat(profile.name, [MediumIcons.BREATH, MediumIcons.HOLD], 'Inspirium Hold Time[ms]',
                                     profile.inspirium_hold_time),
        generate_profile_single_stat(profile.name, [MediumIcons.BREATH, MediumIcons.LEFT_BROKEN_ARROW],
                                     'Expirium Time[ms]', profile.expirium_time),
        generate_profile_single_stat(profile.name, [MediumIcons.BREATH, MediumIcons.HOLD], 'Expirium Hold Time[ms]',
                                     profile.expirium_hold_time),
        generate_profile_single_stat(profile.name, [MediumIcons.LUNGS], 'Tidal Volume[liter]', profile.tidal_volume),
        generate_profile_single_stat(profile.name, [MediumIcons.TIME], 'Profile Run Time[seconds]', profile.time_span),
    ]


def generate_profile_card(profile: Profile):
    return html.Div([
        html.Label(profile.name, className='flex',
                   style={'justify-content': 'center', 'font-size': '20px', 'font-weight': 'bold'}),
        html.Hr(style={'margin': '5px'}),
        html.Div(generate_profile_details(profile))
    ], style={'padding': '10px', 'margin': '5px', 'height': 'fit-content', 'border': '1px solid',
              'border-radius': '10px'})


profiles_grid = html.Div([],
                         style={'display': 'grid', 'grid-gap': '10px',
                                'grid-template-columns': '200px 200px 200px 200px',
                                'height': 'fit-content'}, id=ProfileGrid.ID)


@callback(Output(ProfileGrid.ID, 'children'),
          Input(ProfileForm.ADD_BUTTON, 'n_clicks'))
def update_profile_list(new_profile_button: int):
    return [generate_profile_card(profile) for profile in DatabaseManager().profile_manager.profiles.values()]
