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
    html.P("The purpose of this project is to use machine learning to forecast wheat prices based on historical data. Coming from a farming background, I aim to comprehend the factors influencing prices while employing my knowledge to develop an accurate forecasting model. The project will encompass end-to-end data pipelines, from data extraction to model deployment, and eventually, a website for displaying the results. These results will be accessible once the project is completed, along with the application and the source code."),
    html.Img(src=f'/assets/{image_data[0]["filename"]}', style={'max-width': '100%'}),
    html.P(children=image_data[0]["caption"], style={'text-align': 'center'}),

    html.H3("Methodology",  className="header-text-color", style={'margin-top': '1cm'}),
    html.H5("Data collection", style={'margin-top': '1cm'}),

    html.H5("Data preprocessing", style={'margin-top': '1cm'}),

    html.H5("Univariate analysis", style={'margin-top': '1cm'}),
    html.P("A univariate analysis of wheat prices will be conducted. This analysis will enable us to comprehend the price trends."),

    html.H5("Multivariate analysis", style={'margin-top': '1cm'}),
    html.P("The price of wheat is influenced by multiple time series variables. You can observe these different variables in the first set of charts or pictures."),

    html.H5("Develop the model", style={'margin-top': '1cm'}),
     html.P("A multivariate time series will be used (for example Long Short-term Memory (LSTM) networks, a special type of Recurrent Neural Networks."),

    html.H5("Deploy the model", style={'margin-top': '1cm'}),
    html.P("The model will be deployed using Git and Heroku, the dasboard will be created with Dash python."),
 
], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify', 'margin-bottom': '2cm'})
