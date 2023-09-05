from dash import html


image_data = [
    {"filename": "wheat_price_introduction.png", "caption": "Factors influencing the price of wheat"}
]


layout = html.Div([
    html.Br(),
    html.A(html.Button("Return"), href="/projects"),
    html.H1("Forecasting Wheat Price", style={'margin-top': '1cm'}),
    html.Br(),
    html.Ul([
    html.Li("Date: Current Project"),
    html.Li("Type of Project: Personal"),
    html.Li("Software:  Python, Git, Dash, Heroku"),
    html.Li("Category : Forecast, Time series, Data analysis"),
    ]),
    
    html.Hr(),  
    
    html.H3("Introduction",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P("The purpose of this project is to use machine learning to forecast the wheat prices based on historical data. Coming from a farming background, I would like to understand the factors influencing the price, as well as using my knowledge to develop an accurate forecast model. The project is going to be an end-to-end data pipelines, from data extraction to model deployment to website to display the results."),
    html.Img(src=f'/assets/{image_data[0]["filename"]}', style={'max-width': '100%'}),
    html.P(children=image_data[0]["caption"], style={'text-align': 'center'}),

    html.H3("Methodology",  className="header-text-color", style={'margin-top': '1cm'}),
    html.H5("Data collection", style={'margin-top': '1cm'}),

    html.H5("Data preprocessing", style={'margin-top': '1cm'}),

    html.H5("Univariate analysis", style={'margin-top': '1cm'}),
    html.P("First an univariate analysis of the price of wheat will be held. It allows to understand the trend of the price."),

    html.H5("Multivariate analysis", style={'margin-top': '1cm'}),
    html.P("The price of wheat is influencing by multiple time series variables. Thus, a multivariate time series will be used (for example Long Short-term Memory (LSTM) networks, a special type of Recurrent Neural Networks."),

    html.H5("Develop the model", style={'margin-top': '1cm'}),
     html.P("A multivariate time series will be used (for example Long Short-term Memory (LSTM) networks, a special type of Recurrent Neural Networks."),

    html.H5("Deploy the model", style={'margin-top': '1cm'}),
    html.P("The model will be deployed using Git and Heroku, the dasboard will be created with Dash python."),
 
], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify', 'margin-bottom': '2cm'})
