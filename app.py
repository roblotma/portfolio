import os
import dash_auth
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from pages import home, cv, contact, portfolio, publications
from pages.projects import car_sharing, credit_card, wheat_price
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



def get_layout(pathname):
    layout_mapping = {
        '/home': home.layout,
        '/cv': cv.layout,
        '/publications': publications.layout,
        '/contact': contact.layout,
        '/projects': portfolio.layout,
        '/projects/car_sharing': car_sharing.layout,
        '/projects/credit_card': credit_card.layout,
        '/projects/wheat_price': wheat_price.layout
    }
    return layout_mapping.get(pathname, home.layout)


def display_page(pathname):
    return get_layout(pathname)


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))