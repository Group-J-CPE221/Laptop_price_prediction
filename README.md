# Laptop_price_prediction

The project trained two models :Linear Regression and Random Forest Regression.  
After evaluation,Random Forest outperformed Linear Regression and was used as final deployed model

## Deployment

The Streamlit app for this project is live here:  
[Laptop Price prediction app] (https://laptoppriceprediction-wtjq6qfyt8x8wcozgrmcsm.streamlit.app)

## Files in this Repository
- 'app.py' → Streamlit app code  
- 'random_forest_regression_model.pkl' → Trained machine learning model for random forest regression
- 'rf_model_columns.pkl' → Columns used during model training for random forest regression
- 'requirements.txt' → Dependencies for deployment  
- 'random_forest_regression_model_GroupJ.ipynb' → Jupyter Notebook with data preprocessing, training, and evaluation for random forest regression
- 'Group J list.xslx' → A list of Group J memebers containing the required information
- 'Laptop_price_model.pkl' → Trained machine learning model for linear regression
- 'model_columns.pkl' → Columns used during model training for linear regression
- 'Laptop_Price_Prediction_GroupJ.ipynb' → Jupyter Notebook with data preprocessing, training, and evaluation for linear regression
- 'Mini - Project Report Group J' → Summarizes the entire workflow(EDA,model building and evaluation) and provides instructions on how to use the deployed streamlit app
- 'random_forest_regression_model_Updated.ipynb' → Jupyter Notebook with data preprocessing, training, and evaluation for random forest regression with updated random state of 28
- 'rf_model_columns_Updated.pkl' → Columns used during model training for random forest regression with updated random state of 28
- 'random_forest_regression_model_Updated.pkl' → Trained machine learning model for random forest regression with updated random state of 28
- 'linear_regression_model.ipynb' → Jupyter Notebook with data preprocessing, training, and evaluation for linear regression with updated random state of 28
- 'lr_model_columns.pkl' → Columns used during model training for linear regression with updated random state of 28
- 'linear_regression_model.pkl' → Trained machine learning model for linear regression with updated random state of 28
- 'Mini - Project Report Group J Updated' → Summarizes the entire workflow(EDA,model building and evaluation) and provides instructions on how to use the deployed streamlit app with Updated Model building and Evaluation values

  ## Note
  All files with "Updated" as part of their name are the actual files as random state was corrected from 42 to 28 including linear_regression_model.ipynb, lr_model_columns.pkl, linear_regression_model.pkl.
