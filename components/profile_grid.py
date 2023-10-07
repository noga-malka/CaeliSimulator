from dash import html, callback, Output, Input

from components.consts import ProfileGrid, ProfileForm
from database.database_manager import DatabaseManager
from models.profile import Profile


def generate_profile_card(profile: Profile):
    return html.Div([
        html.Label(profile.name),
        html.Hr(),
        html.Div('', className='flex center')
    ], style={'padding': '10px', 'margin': '5px', 'height': 'fit-content', 'border': '1px solid',
              'border-radius': '10px'})


profiles_grid = html.Div([],
                         style={'display': 'grid', 'grid-gap': '10px', 'grid-template-columns': '100px 100px 100px',
                                'height': 'fit-content'}, id=ProfileGrid.ID)


@callback(Output(ProfileGrid.ID, 'children'),
          Input(ProfileForm.ADD_BUTTON, 'n_clicks'))
def update_profile_list(new_profile_button: int):
    return [generate_profile_card(profile) for profile in DatabaseManager().profile_manager.profiles.values()]
