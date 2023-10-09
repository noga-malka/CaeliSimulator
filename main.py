import dash_bootstrap_components
from dash import Dash

from database.database_manager import DatabaseManager

database_manager = DatabaseManager()
app = Dash(__name__,
           external_stylesheets=[dash_bootstrap_components.themes.FLATLY],
           suppress_callback_exceptions=True,
           use_pages=True,
           title='Caeli')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
