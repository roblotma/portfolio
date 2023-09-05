from dash import html


image_data = [
    {"filename": "carsharing_results1.png", "caption": "Caption 1"},
    {"filename": "carsharing_results2.png", "caption": "Caption 2"},
    {"filename": "carsharing_results3.png", "caption": "Accessibility indicator by walking in 20 minutes"},
    {"filename": "carsharing_results4.png", "caption": "Accessibility indicator by multimodal transport in 20 minutes"},
    {"filename": "carsharing_results5.png", "caption": "Correlation coefficient between vehicle accessibility and active member ratio by dissemination area, compared with cumulative opportunities (CO) and weighted opportunities (WO)"},
    {"filename": "carsharing_results6.png", "caption": "Multiple linear regression"},
    {"filename": "carsharing_data.png", "caption": "Data source"},
    {"filename": "carsharing_methodology.png", "caption": "Methodology"},
]


layout = html.Div([
    html.Br(),
    html.A(html.Button("Return"), href="/projects"),
    html.H1("Car Sharing: An Analysis of the Influence of Walking and Public Transport Accessibility", style={'margin-top': '1cm'}),
    html.Br(),
    html.Ul([
    html.Li("Date: September 2019 - February 2020"),
    html.Li("Type of Project: Internship as Research Assistant at Polytechnique Montreal"),
    html.Li("Software: R-studio, ArcGIS"),
    html.Li("Category: Data Wrangling, Data Exploration, ArcGIS Spatial Tools, Machine Learning"),
    ]),
    
    html.Hr(),  
    
    html.H3("Introduction",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P("In the context of sustainable mobility policies, carsharing services have gained importance as an alternative to personal vehicles. In an effort to increase the adherence to and use of such services, several studies have explored the key factors that determine use and membership. While the ease with which individuals can access shared vehicles appears to be a central determinant, few studies have specifically investigated how to measure station and vehicle accessibility. To fill this gap, this study seeks to systematically assess and compare the contribution of different accessibility indicators to modeling carsharing adhesion, using 2016 data from the Montreal carsharing company Communauto and from the Canadian census."),

    html.H3("Data",  className="header-text-color", style={'margin-top': '1cm'}),
    html.Img(src=f'/assets/{image_data[6]["filename"]}', style={'max-width': '100%'}),

    html.H3("Methodology",  className="header-text-color", style={'margin-top': '1cm'}),
    html.Img(src=f'/assets/{image_data[7]["filename"]}', style={'max-width': '100%'}),
    
    html.H3("Results",  className="header-text-color", style={'margin-top': '1cm'}),
    html.Br(),
    html.P("The results show that walking accessibility, within 20 minutes, and public transport accessibility, within 40 minutes, are both key determinants of membership rate and in a complementary manner. The influence of public transport accessibility is positive and highest when walking accessibility is low. The results also demonstrate that the use of a cumulative or weighted opportunity indicator is equally sound from an empirical perspective. The study is of relevance to researchers and planners wishing to better understand and model the influence of vehicle accessibility."),
    html.Br(),
    
    html.Img(src=f'/assets/{image_data[2]["filename"]}', style={'max-width': '100%'}),
    html.P(children=image_data[2]["caption"], style={'text-align': 'center'}),
    html.Br(),

    html.Img(src=f'/assets/{image_data[4]["filename"]}', style={'max-width': '100%'}),
    html.P(children=image_data[4]["caption"], style={'text-align': 'center'}),
    html.Br(),

    html.Img(src=f'/assets/{image_data[5]["filename"]}', style={'max-width': '100%'}),
    html.P(children=image_data[5]["caption"], style={'text-align': 'center'}),
    html.Br(),

    html.A("Article", href="https://journals.sagepub.com/doi/abs/10.1177/03611981211032221?journalCode=trra", target="_blank"),


], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify', 'margin-bottom': '2cm'})
