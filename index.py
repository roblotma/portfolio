import dash_bootstrap_components as dbc


navbarportfolio = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Resume", href="/cv")),
            dbc.NavItem(dbc.NavLink("Portfolio", href="/projects")),
            dbc.NavItem(dbc.NavLink("Publications", href="/publications")),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        ],
        brand="Portfolio Mathilde Roblot",  
        brand_href="/home",  
        sticky="top", 
        color="primary", 
        dark=True,  
    )