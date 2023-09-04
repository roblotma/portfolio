import dash_bootstrap_components as dbc


navbarportfolio = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("CV", href="/cv")),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Projects", 
                children=[
                    dbc.DropdownMenuItem("Car Sharing", href='/project1'), 
                    dbc.DropdownMenuItem("Project 2", href='/project2'),
                    dbc.DropdownMenuItem("Project 3", href='/project3'),
                ],
            ),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        ],
        brand="Portfolio Mathilde Roblot",  
        brand_href="/home",  # Set the URL where the user will be sent when they click the brand we just created "Home"
        sticky="top", 
        color="primary", 
        dark=True,  
    )