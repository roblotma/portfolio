from dash import html, dcc


layout = html.Div([

    html.Div([
    html.Div([
        # Left column for text
        html.Div([
            html.P(" I am a dedicated Data Scientist with a proven track record in developing data-driven solutions for real estate and urban planning. I am passionate about leveraging data to solve complex problems and deliver valuable insights. Seeking opportunities to contribute my skills and expertise to a dynamic organization."),
        ], style={'width': '50%', 'display': 'inline-block',  'vertical-align': 'middle'}),

        # Right column for the image
        html.Div([
            html.Img(src="assets/PhotoCV.png", style={'max-width': '60%', 'display': 'inline-block', 'vertical-align': 'middle', 'margin': '1.5cm'}),
        ], style={'width': '50%', 'display': 'inline-block',  'vertical-align': 'middle'}),
    ]),


    html.H3([html.Img(src="assets/suitcase.png", style={'height': '1em'})," Experience"], style={'margin-top': '1cm'}, className="header-text-color"),
    html.H5("Data Scientist"),
    html.P([
        "Skenariolabs, Helsinki, Finland",
        html.Br(),
        dcc.Markdown("November 2021 - Present", style={'font-style': 'italic'})
    ]),
    html.Ul([
        html.Li("Spearheaded the development of real estate valuation and energy label models for multiple countries using an ESG-risks analytics approach."),
        html.Li("Established end-to-end data pipelines, from data extraction to model deployment, utilizing Bitbucket and AWS technologies."),
        html.Li("Effectively communicated analysis results and provided actionable recommendations to both internal teams and clients."),
    ]),

    html.H5("Urban Data Scientist Intern"),
    html.P([
        "EP, Nantes, France",
        html.Br(),
        dcc.Markdown("February 2021 - August 2021", style={'font-style': 'italic'})
    ]),
    html.Ul([
        html.Li("Successfully identified and implemented data-driven opportunities from various urban sources to enhance decision-making processes."),
        html.Li("Constructed predictive models related to real estate and urban regulations using ArcGIS."),
        html.Li("Innovated by creating a new application for real estate prospecting with the integration of PostGIS and MapBox technologies."),
    ]),
    html.H5("Research Intern"),
    html.P([
        "Polytechnique Montréal, Montréal, Canada",
        html.Br(),
        dcc.Markdown("September 2019 - February 2020", style={'font-style': 'italic'})
    ]),
    html.Ul([
        html.Li("Conducted in-depth research and analysis to comprehend and predict carsharing membership trends in Montreal."),
        html.Li("Developed a regression model utilizing user characteristics and urban planning variables to forecast carsharing membership rates."),
    ]),

    html.H3([html.Img(src="assets/school.png", style={'height': '1em'})," Education"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    
    html.H5("Master of Science In Data Science"),
    html.P([
        "Université de Technologie de Compiègne, Compiègne, France",
        html.Br(),
        dcc.Markdown("2020 - 2021", style={'font-style': 'italic'})
    ]),
    html.Ul([html.Li("Subjects included: Data mining, Machine and deep learning, Decision theory, Robust and stochastic optimization, Multi-criteria decision under uncertainties, In-depth mathematics"),]),
    html.H5("Master’s Degree in Urban Engineering"),
    html.P([
        "Université de Technologie de Compiègne, Compiègne, France",
        html.Br(),
        dcc.Markdown("2016 - 2021", style={'font-style': 'italic'})
    ]),

    html.Ul([
        html.Li("Subjects included: Technical management with social and legal dimensions of buildings, Town planning and development, Modeling and construction, Network optimization"),
        html.Li("Minor: International economics - micro- and macroeconomic, accounting, international organizations and business strategy")]),

    html.H5("Exchange semester in Master of Urban Spatial Planning "),
    html.P([
        "Technische Universität Dortmund",
        html.Br(),
        dcc.Markdown("2018", style={'font-style': 'italic'})
    ]),
    

    html.H3([html.Img(src="assets/pencil.png", style={'height': '1em'})," Skills"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    html.Img(src=f'/assets/skills.png', style={'max-width': '100%'}),

    html.H3([html.Img(src="assets/language.png", style={'height': '1em'})," Language"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    html.Img(src=f'/assets/skills_language.png', style={'max-width': '30%', 'margin':'1cm'}),
    
    html.Br(),

   ], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify'}),
   html.Div([
       html.A(html.Button("Download my resume", id='download-button'), href='assets/resume.pdf', download='resume_mathilde_roblot.pdf', style={'margin-top': '1.5cm', 'text-align': 'left'})]
       , style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'center', 'margin-bottom': '1.5cm'})
   ])
