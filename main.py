import dash
import dash_bootstrap_components
from dash import Dash, html

from components.navigation_bar import navigation_bar
from components.placeholder import placeholder
from components.simulator_components.control_buttons import control_buttons
from components.title import title
from database.database_manager import DatabaseManager
from simulator_data_manager.simulator_data_manager import SimulatorDataManager

app = Dash(__name__,
           external_stylesheets=[dash_bootstrap_components.themes.FLATLY],
           suppress_callback_exceptions=True,
           use_pages=True,
           title='Caeli')

app.layout = html.Div([
    title,
    placeholder,
    html.Div([navigation_bar,
              html.Div([control_buttons,
                        dash.page_container],
                       className='full-width')],
             className='flex', style={'height': '100vh'})])

if __name__ == '__main__':
    SimulatorDataManager()
    DatabaseManager()
    app.run(host='0.0.0.0', debug=True)
