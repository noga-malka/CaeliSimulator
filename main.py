import dash_bootstrap_components
from dash import Dash

app = Dash(__name__,
           external_stylesheets=[dash_bootstrap_components.themes.DARKLY],
           suppress_callback_exceptions=True,
           title='Caeli')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
