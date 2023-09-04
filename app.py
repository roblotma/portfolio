import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from pages import home, cv, contact, car_sharing
from dash.dependencies import Input, Output

from index import navbarportfolio

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, '/assets/config.css'])
app.title = "Portfolio Mathilde Roblot"


# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbarportfolio, 
    html.Div(id='page-content', children=[]), 
])

# Create the callback to handle mutlipage inputs
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])


def display_page(pathname):
    if pathname == '/home':
        return home.layout
    if pathname == '/cv':
        return cv.layout
    if pathname == '/contact':
        return contact.layout
    if pathname == '/project1':
        return car_sharing.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run(debug=True)