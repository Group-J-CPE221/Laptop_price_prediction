# Laptop Price Prediction

Predicts laptop prices using machine learning with comprehensive feature engineering and exploratory data analysis.

## Model Performance

**Final Model:** Random Forest Regressor  
**Metrics:**
- **RMSE:** 3.52
- **MAE:** 1.84
- **R²:** 1.00
- **Training R²:** 0.9999

## Dataset

**Source:** Kaggle – Laptop Price Dataset by muhammetvarl  
**Size:** 1,303 entries with 13 features  
**Target:** Price in Euros (€)  
**Geographic Scope:** European laptop market

## Exploratory Data Analysis (EDA)

Key findings revealed what drives laptop prices:

- **RAM Size:** Strongest single predictor (correlation: 0.74)
- **Brand Reputation:** Razer (~€2,387), LG (~€2,099), Apple (~€1,562) command premium; Acer (~€627), Chuwi (~€314) budget-tier
- **Laptop Type:** Workstations (~€2,158) and Gaming (~€1,669) are premium; Notebooks (~€779) and Netbooks (~€636) are budget
- **Operating System:** MacOS (~€1,747) and Windows (~€1,622) premium; Linux (~€617) and Chrome OS (~€554) budget

## Feature Engineering

Enhanced model interpretability and performance:
- **Log_Price:** Log transformation to reduce skewness
- **Screen_Area:** Calculated from screen diagonal
- **Price_per_GB:** Price normalized by RAM capacity
- **Portability Index:** Weight ÷ screen size ratio
- **Is_Touchscreen:** Binary touchscreen indicator
- **OS_Category:** Grouped operating systems
- **Is_Gaming / Is_Workstation:** Binary laptop category flags

## Methodology

**Data Processing:**
- Handled outliers using IQR method
- Applied label encoding and one-hot encoding for categorical variables
- 80/20 train-test split

**Model Selection:**
- Evaluated Linear Regression (baseline) — R² 0.95 but produced unrealistic negative prices
- Selected Random Forest Regressor (100 estimators, random_state=42) — robust, realistic predictions

## Deployment

**Live App:** [Laptop Price Prediction](https://laptoppriceprediction-wtjq6qfyt8x8wcozgrmcsm.streamlit.app)

Enter laptop specifications (brand, RAM, OS, screen type) to get real-time price predictions.

**Tech Stack:**
- Python (pandas, scikit-learn, numpy)
- Streamlit (interactive deployment)
- Jupyter Notebook (development & analysis)

## Repository Files

- `random_forest_regression_model.ipynb` — Full data processing, EDA, feature engineering, model training & evaluation
- `app.py` — Streamlit web application
- `random_forest_regression_model.pkl` — Trained Random Forest model
- `rf_model_columns.pkl` — Feature columns for inference
- `requirements.txt` — Python dependencies
