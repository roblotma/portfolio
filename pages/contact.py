from dash import html


layout = html.Div([
    html.Div([
        html.Img(src="assets/email.png", style={'max-width': '10%', 'margin-top': '1cm'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}),

    html.P("Feel free to contact me for any question", style={'margin-top': '1cm'}),

    html.H5("LinkedIn", style={'margin-top': '1cm'}),
    html.A("LinkedIn Profile", href="https://www.linkedin.com/in/mathilde-roblot", target="_blank"),

    html.H5("Email", style={'margin-top': '1cm'}),
    html.A("mathilderoblot4@gmail.com", href="mailto:mathilderoblot4@gmail.com"),

    html.H5("Phone", style={'margin-top': '1cm'}),
    html.P("(+33) 40 32 80 65"),
    html.P("(+358) 40 680 1523"),
    
    html.H5("Address", style={'margin-top': '1cm'}),
    html.P("Malminkatu 5, Helsinki, Finland"),
    
], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'center'})
