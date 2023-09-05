from dash import html


layout = html.Div([
    html.Br(),
    html.H3(["Peer-Reviewed Journal"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    html.P("Roblot, M., Boisjoly, G., Francesco, C., & Martin, T. (2021). Participation in Shared Mobility: An Analysis of the Influence of Walking and Public Transport Accessibility to Vehicles on Carsharing Membership in Montreal, Canada. Transportation Research Record, 03611981211032221."),
    html.A("Article", href="https://journals.sagepub.com/doi/abs/10.1177/03611981211032221?journalCode=trra", target="_blank"),

    html.H3(["Presentation"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    html.P("Roblot, M., Boisjoly, G., Francesco, C., & Martin, T. Vehicles on Carsharing Membership in Montreal, Canada. Poster presented at: TRB Annual Meeting; January 2021; Washington, United States"),
    html.P("Roblot M. Accessibilité à la mobilité partagée: une analyse des modalités d'urbanisme déterminant l'adhésion au service d'autopartage. Poster presented at: RFTM; June 2021; Paris, France", style={'margin-top': '1cm'}),
], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify'})
