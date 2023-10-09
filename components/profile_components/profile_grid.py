import dash_bootstrap_components
from dash import html, callback, Output, Input
from dash_iconify import DashIconify

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
    breath_icon = DashIconify(icon='openmoji:wind-face', width=32, flip='horizontal')
    arrow_right_icon = DashIconify(icon='solar:arrow-right-broken', width=32)
    arrow_left_icon = DashIconify(icon='solar:arrow-left-broken', width=32)
    hold_icon = DashIconify(icon='bi:pause', width=32)
    lungs_icon = DashIconify(icon='healthicons:lungs-outline', width=32)
    time_icon = DashIconify(icon='carbon:time', width=32)

    return [
        generate_profile_single_stat(profile.name, [breath_icon, arrow_right_icon], 'Inspirium Time[ms]',
                                     profile.inspirium_time),
        generate_profile_single_stat(profile.name, [breath_icon, hold_icon], 'Inspirium Hold Time[ms]',
                                     profile.inspirium_hold_time),
        generate_profile_single_stat(profile.name, [breath_icon, arrow_left_icon], 'Expirium Time[ms]',
                                     profile.expirium_time),
        generate_profile_single_stat(profile.name, [breath_icon, hold_icon], 'Expirium Hold Time[ms]',
                                     profile.expirium_hold_time),
        generate_profile_single_stat(profile.name, [lungs_icon], 'Tidal Volume[liter]', profile.tidal_volume),
        generate_profile_single_stat(profile.name, [time_icon], 'Profile Run Time[seconds]', profile.time_span),
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
