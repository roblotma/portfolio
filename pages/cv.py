from dash import html


layout = html.Div([
    html.Br(),
    html.P("I am a dedicated Data Scientist with a proven track record in developing data-driven solutions for real estate and urban planning. I am passionate about leveraging data to solve complex problems and deliver valuable insights. Seeking opportunities to contribute my skills and expertise to a dynamic organization."),

    html.H3([html.Img(src="assets/suitcase.png", style={'height': '1em'})," Experience"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    html.H5("Data Scientist at Skenariolabs, Helsinki, Finland"),
    html.P("November 2021 - Present"),
    html.Ul([
        html.Li("Spearheaded the development of real estate valuation and energy label models for multiple countries using an ESG-risks analytics approach."),
        html.Li("Established end-to-end data pipelines, from data extraction to model deployment, utilizing Bitbucket and AWS technologies."),
        html.Li("Effectively communicated analysis results and provided actionable recommendations to both internal teams and clients."),
    ]),

    html.H5("Urban Data Scientist Intern at EP, Nantes, France"),
    html.P("February 2021 - August 2021"),
    html.Ul([
        html.Li("Successfully identified and implemented data-driven opportunities from various urban sources to enhance decision-making processes."),
        html.Li("Constructed predictive models related to real estate and urban regulations using ArcGIS."),
        html.Li("Innovated by creating a new application for real estate prospecting with the integration of PostGIS and MapBox technologies."),
    ]),

    html.H5("Research Intern at Polytechnique Montréal, Montréal, Canada"),
    html.P("September 2019 - February 2020"),
    html.Ul([
        html.Li("Conducted in-depth research and analysis to comprehend and predict carsharing membership trends in Montreal."),
        html.Li("Developed a regression model utilizing user characteristics and urban planning variables to forecast carsharing membership rates."),
    ]),

    html.H3([html.Img(src="assets/school.png", style={'height': '1em'})," Education"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    
    html.H5("Master of Science In Data Science (2020 - 2021)"),
    html.P("Université de Technologie de Compiègne, Compiègne, France"),
    html.P("Subjects included: Data mining, Machine and deep learning, Decision theory, Robust and stochastic optimization, Multi-criteria decision under uncertainties, In-depth mathematics"),
    
    html.H5("Master’s Degree in Urban Engineering (2016 - 2021)"),
    html.P("Université de Technologie de Compiègne, Compiègne, France"),
    html.P("Subjects included: Technical management with social and legal dimensions of buildings, Town planning and development, Modeling and construction, Network optimization"),
    html.P("Minor: International economics - micro- and macroeconomic, accounting, international organizations and business strategy"),
    
    html.H5("Exchange semester in Master of Urban Spatial Planning (2018)"),
    html.P("Technische Universität Dortmund, Dortmund, Germany"),
    

    html.H3([html.Img(src="assets/pencil.png", style={'height': '1em'})," Skills"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    html.Ul([
        html.Li("Programming Languages: Python, R"),
        html.Li("Data Analysis & Visualization: Pandas, Numpy, Matplotlib, Seaborn, Dash"),
        html.Li("Machine Learning: Scikit-Learn, XGBoost, TensorFlow"),
        html.Li("Database Technologies: SQL, PostGIS, pgAdmin"),
        html.Li("Version control system and cloud computing : AWS, Bitbucket, Git"),
        html.Li("Geographic Information Systems (GIS): ArcGIS, MapBox"),
        html.Li("Communication: Strong presentation and data storytelling skills"),
        html.Li("Languages: French (Mother tongue), English (Fluent C1 - IELTS 7.0), German (Intermediate Level B2)"),
    ]),

    html.H3([html.Img(src="assets/application.png", style={'height': '1em'})," Publication"], style={'margin-top': '1.5cm'}, className="header-text-color"),
    html.H5("Peer-Reviewed Journal"),
    html.P("Roblot, M., Boisjoly, G., Francesco, C., & Martin, T. (2021). Participation in Shared Mobility: An Analysis of the Influence of Walking and Public Transport Accessibility to Vehicles on Carsharing Membership in Montreal, Canada. Transportation Research Record, 03611981211032221."),
    html.A("Article", href="https://journals.sagepub.com/doi/abs/10.1177/03611981211032221?journalCode=trra", target="_blank"),
    html.Br(),
    html.H5("Presentation"),
    html.P("Roblot, M., Boisjoly, G., Francesco, C., & Martin, T. Vehicles on Carsharing Membership in Montreal, Canada. Poster presented at: TRB Annual Meeting; January 2021; Washington, United States"),
    html.P("Roblot M. Accessibilité à la mobilité partagée: une analyse des modalités d'urbanisme déterminant l'adhésion au service d'autopartage. Poster presented at: RFTM; June 2021; Paris, France"),
], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify'})
