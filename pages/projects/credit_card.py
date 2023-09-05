from dash import html, dcc


image_data = [
    {"filename": "credit_card_results.png", "caption": "Performance measurement of different algorithms (accuracy, performance, recall and f1 score) with different resampling methods (normal, under, over and SMOTE)"},
     {"filename": "credit_card_conclusion.png", "caption": "Comparison between different prediction methods according to the performance"}
]


layout = html.Div([
    html.Br(),
    html.A(html.Button("Return"), href="/projects"),
    html.H1("Default credit card clients", style={'margin-top': '1cm'}),
    html.Br(),
    html.Ul([
    html.Li("Date: February 2020 - June 2020"),
    html.Li("Type of Project: School Project"),
    html.Li("Sofware: PyCharm, Git"),
    html.Li("Category:  Data analysis, Machine learning algorithms (logistic regression, K nearest neighbors, binary tree, random forest and artificial neural network)"),
    ]),
    
    html.Hr(),  
    
    html.H3("Introduction",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P(["This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in a bank in Taiwan from April 2005 to September 2005. The objective of the project is to implement a pro-active directive to prevent the risk of default in the payments of bank customers.", html.Br(), "Different machine learning algorithms have be tested in order to see which method best estimates the possible default of credit card holders."]),

    html.H3("Data",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P(["The data sample consists of 30,000 credit card holders. The period of analysis of bank data for these individuals is from April 2005 to September 2005. Quantitative bank account data is expressed in New Taiwan Dollar (NT$).",  html.Br(), "The variable to explain is the default, def_pay, which is a binary variable, 0 for a person without default and 1 for a person in default. To explain this variable, individuals are described with 23 explanatory variables :"]),
    html.Ul([
        html.Li("quantitative variables : credit limit, age, payment history per month, bill statement amount, etc."),
        html.Li("qualitative variables : sex, marriage, education, etc."),
        ]),
    html.A("Dataset", href="https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients", target="_blank"),


    html.H3("Methodology",  className="header-text-color", style={'margin-top': '1cm'}),
    html.H5("Data preprocessing", style={'margin-top': '1cm'}),
    html.P([dcc.Markdown("Cleaning", style={'font-style': 'italic'})]),
    html.P(["There is no missing data.", 
            html.Br(), 
            "The MARRIAGE and EDUCATION variables can take values whose meaning we don't know in the description of the data set. Therefore, these unknown values have been replaced by a modality having the other meaning.", html.Br(),"The variables PAY_x can take the values -2 and 0, our knowledge of the functioning of the credit card sector didn't allow us to fully understand these values. -2 and 0 correspond to people who aren't late in payment, as well as -1, which is why we have chosen to group -2, -1 and 0 under the same modality 0, meaning duly paid."]),
    
    html.P([dcc.Markdown("Transformation", style={'font-style': 'italic'})]),
    html.P(["Standardization : the dataset contains data that has widely varying values in amplitudes and units between them. Most machine learning algorithms use the Euclidean distance between two data points in their calculation, such as K-Nearest-Neighbors, SVM, and Neural Network. Scaling the features of our model is extremely essential, especially when the variation in scale between different features is very large. Otherwise, the large variation features will have a big influence in the distance calculation.", 
            html.Br(), 
            html.Br(), 
            "One hot encoding : regarding the variables of gender and marital status, we carried out one hot encoding because there is no relationship between the values taken. Instead of having a single column for these variables, there will be as many columns as there are possible categories. The value taken will be either 0 or 1 depending on the absence or presence of this modality for the individual."]),
    
    html.P([dcc.Markdown("Reduction", style={'font-style': 'italic'})]),
    html.P("We used the PCA method to perform the data reduction. PCA is a statistical method that reduces the number of attributes by grouping strongly correlated attributes."),
    
    html.H5("Data modeling and evaluation", style={'margin-top': '1cm'}),
    html.P("This sample includes 30,000 individuals with credit cards. Of these individuals, 6,636 are in default after 6 months, i.e. the proportion of default in the data is 22.1%. Thus, in this classification problem, individuals in default are under-represented compared to others. The machine learning model isn't penalized enough if it doesn't take it into account. We need to balanced the dataset."),
    html.Ul([
        html.Li("Separation of the dataset into a training sample and a test sample"),
        html.Li("Resampling in order to have a balanced dataset using 3 methods : aleatory under sampling, aleatory oversampling and oversampling with SMOTE"),
        html.Li("Modeling the training with binary tree / random forest, KNN, logistic regression and neural network. "),
        ]),

    html.P(["In order to have a model and performance not biased by training a single sample, we do a cross-validation. We have carried out the k-fold cross-validation technique.", 
            html.Br(), 
            html.Br(), 
            "Then a confusion matrix is used as a tool for measuring performance and comparing all machine learning algorithms, using accuracy, precision, F1 score and recall."]),

    html.H3("Results",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P("Data on payment history is strongly correlated (R2 = 0,8) between different months, as are invoices for different months. This shows that people have similar buying trends over the 6 month period. The other data are weakly correlated with each other (R2 <0.2)."),
    
    html.H5("KNN", style={'margin-top': '1cm'}),
    html.P("In order to find the best number of neighbors, we used the gridSearchCV() with the criteria AUC obtained with the ROC curve. With a 10 folds cross validation, 71 is the best number of neighbors for the unbalanced sample, 59 for the under sampling, 365 for the oversampling and 322 for the smote sample."),

    html.H5("Random Forest", style={'margin-top': '1cm'}),
    html.P("To improve the performance of a decision tree, we tested the random forest algorithm. Its principle is to reduce the variance of forecasts from a single decision tree. Thus, it performs parallel learning on multiple decision trees built randomly and trained on different data subsets. A test is done for the number of trees in the forest varying from 15 to 175. It can be seen that after 100, the OOB out-of-bag error rate begins to stabilize. So we finally choose 130."),

    html.H5("Neural network", style={'margin-top': '1cm'}),
    html.Ul([
        html.Li("Activation function : RELU"),
        html.Li("Output function : sigmoid "),
        html.Li("Optimization : Adam"),
        html.Li("Complexity : Dropout method"),
        ]),

    html.Img(src=f'/assets/{image_data[0]["filename"]}', style={'max-width': '100%'}),
    html.P(children=image_data[0]["caption"], style={'text-align': 'center'}),

    html.H3("Conclusion",  className="header-text-color", style={'margin-top': '1cm'}),
    html.P("The figure above makes it possible to compare the performances of the 5 prediction models according to 5 criteria: AUC, accuracy, precision, recall and F1-Score, during the test of data. To compare, we took the data sets of learning transformed with the algorithm SMOTE. Indeed, the performance values were the best with this learning data."),
    
    html.Img(src=f'/assets/{image_data[1]["filename"]}', style={'max-width': '100%'}),
    html.P(children=image_data[1]["caption"], style={'text-align': 'center'}),

    html.P(["Comparison shows AUC and accuracy the 2 highest performance criteria to each time in the prediction models. However no model really stands out. It's about choosing according to the criteria that we put forward as the preference to predict good accuracy or else predict when a person may be at fault.", 
        html.Br(), 
        html.Br(), 
        "The amount and imbalance of data has caused us given the opportunity to learn more about the need and the different pre-treatment methods before implement them in a prediction model. So this project made us make choices about the treatment data, which can be discussed as needed interpretation of results. For example, the use of the PCA has resized the data but we do not can't know what exactly are the variables of bases which have an impact or not on the failure of payment in the prediction model."]),
 
], style={'margin-left': '10cm', 'margin-right': '10cm', 'text-align': 'justify', 'margin-bottom': '2cm'})
