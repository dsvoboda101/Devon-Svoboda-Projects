# Modelling User Engagement to Identify Features of Active Users
### Mock Interview Challenges for Springboard Data Science Certification

As part of the final evaluation for the Springboard Data Science Certification, these assignments were designed to mimic data science challenges posed during technical interviews. The three projects below demonstrate data visualization and modelling skills applied to simulated user datasets drawn from business contexts outside of health care and biotech.

---

## Projects

### 1. 📈 [Website User Logins](./Website_logins)

**Goal:** Characterize patterns in website usage from login timestamps and make business recommendations.

Using a JSON file of simulated user login timestamps, login counts were aggregated into 15-minute intervals and analyzed using time series methods. The analysis revealed clear daily and weekly periodicity: a strong late-night/early-morning usage peak, a secondary midday spike, and substantially higher weekend activity concentrated between 1–5 AM Saturday and Sunday mornings. Statistical testing confirmed a significant increase in evening usage from Monday through Thursday (≈+1.86 logins per 15-minute interval per day), with weekend overnight peaks being significantly higher than weekday equivalents. Findings were interpreted to suggest a younger, non-9-to-5 user base (consistent with a gaming or entertainment platform) and used to make server resource recommendations.

**Key techniques:** Time series aggregation, cyclic decomposition (daily/weekly), OLS regression, Tukey HSD post-hoc testing, visualization with Matplotlib and Seaborn.

---

### 2. 🚗 [Rideshare User Feature Evaluation](./Rideshare_Active_User_Identification)

**Goal:** Identify the strongest predictors of rider retention for a rideshare company and offer actionable marketing recommendations.

Working with a dataset of ~50,000 simulated users who signed up in January 2014, active users were defined as those who took a trip in the 30 days preceding the data pull. Exploratory analysis included outlier detection, missing value imputation, and feature engineering from datetime columns. Three classifiers were screened — Random Forest, XGBoost, and CatBoost — all achieving strong ROC-AUC scores (RF: 0.830, XGB: 0.852, CB: 0.857). XGBoost was selected for hyperparameter tuning via `RandomizedSearchCV` due to its speed-performance balance. SHAP values were used to interpret the final model and describe the features most predictive of user retention.

**Key techniques:** Data cleaning & EDA, Full Classification Model Pipelines, Scikit-learn pipelines, ROC-AUC, confusion matrix, SHAP feature importance.

---

### 3. 🔍 [Relax Data Science Challenge](./Relax_Data_Science_Challenge)

**Goal:** Define "active" users from raw login data, build a predictive model from user metadata, and deliver marketing recommendations.

This challenge used two datasets: user metadata and login engagement records. Active users were defined using a rolling 7-day window such that any user with 3 or more logins in any 7-day period was labeled active. This target was merged with the user metadata table. Given class imbalance (~5:1 inactive to active), F1 score was used as the primary tuning metric alongside ROC-AUC. XGBoost outperformed Random Forest across all metrics, particularly in recall and F1. Hyperparameter tuning with `scale_pos_weight` to address class imbalance and SHAP analysis identified the features which were top predictors of user status.  The analysis concluded that longer-tenured users and those with recent sessions being significantly more likely to be active. A written summary of findings and marketing recommendations was provided to the client.

**Key techniques:** Rolling window time series analysis, data merging, imbalanced classification, Scikit-learn pipelines, confusion matrix visualization, SHAP summary plots.

---

## Key Tools & Libraries

| Category | Tools |
|---|---|
| Language | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost, CatBoost |
| Model Interpretability | SHAP |
| Statistical Testing | Statsmodels (OLS, Tukey HSD) |
| Time Series | Rolling windows, 15-min interval aggregation |