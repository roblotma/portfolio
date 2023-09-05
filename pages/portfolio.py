from dash import html


layout = html.Div([
    html.H4("Car sharing",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P("An analysis of the influence of walking and public transport accessibility to vehicles on car sharing membership in Montreal, Canada"),
    html.P("Tools used : R, ArcGIS"),
    html.P("Category :  ArcGIS Spatial Tools, Machine Learning"),
    html.A(html.Button("Read more"), href="/projects/car_sharing"),
    html.Hr(),   

    html.H4("Wheat price prediction",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P("The goal of this project is to use machine learning to predict wheat prices based on historical data."),
    html.P("Tools used : Python, Git, Dash, Heroku"),
    html.P("Category : Forecast, Time series, Data analysis"),
    html.A(html.Button("Read more"), href="/projects/wheat_price"),
    html.Hr(),  

    html.H4("Default of credit card clients",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P("This project consists of the analysis of a customer default of credit card dataset. This dataset was made available on UCI Machine Learning Repository by I-Cheng Yeh."),
    html.P("Tools used : Python, Git"),
    html.P("Category : Classification, Teamwork"),
    html.A(html.Button("Read more"), href="/projects/credit_card"),
    html.Hr(),  

    html.H4("Kaggle Competition",  className="header-text-color", style={'margin-top': '1cm'}),
    html.A("House prices using XGBoost", href="https://www.kaggle.com/code/roblotmathilde/house-prices-using-xgboost/notebook", target="_blank"),


    
], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify'})
