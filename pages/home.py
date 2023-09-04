# Import necessary libraries 
from dash import html


# Define the page layout
layout = html.Div([
    html.Br(),
    html.Div([
        html.Img(src='assets/PhotoCV.png', style={'max-width': '40%', 'height': 'auto', 'display': 'block', 'margin': '0 auto'}), 
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    html.Div([
        html.P("Hello, my name is Mathilde"),
        html.P("Highly motivated with over 3 years of experience in Data Science and Urban Planning, looking for a meaningful role to find creative solutions to exciting problems and have a real-life impact. Experienced at making geospatial and other data useable, using machine learning algorithms to deliver insights and implement action-oriented solutions."),
    ], style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top'})
], style={'margin-left': '5cm', 'margin-right': '5cm', 'text-align': 'justify'})
