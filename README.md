# Devon Svoboda: Data Science Portfolio

I'm a Data Scientist with 8+ years of industry and academic experience in cellular biology, gene and cell therapy, and translational biotech R&D. After reaching Principal Scientist level, I made a deliberate pivot into data science by completing an intensive Python-based bootcamp with Springboard and building skills in machine learning, statistical modeling, SQL, and data analysis.

What differentiates me as a data scientist is my ability to deeply understand the science behind the data. I bring strong scientific intuition to problem formulation, model development, and interpretation, enabling more meaningful insights than analytics alone. I’m particularly interested in applied data science and machine learning roles embedded within R&D, platform development, or discovery teams, where data directly shapes scientific strategy and therapeutic development.

---

## Projects

### 🧬 [Predicting iPSC Differentiation Efficiency](./Prediciting_iPSC_Diff_Efficiency)
**Capstone 3: Springboard Data Science Certification**

Inspired by real challenges encountered at Shoreline Biosciences, this project builds a machine learning pipeline to predict how effectively iPSC donor lines will differentiate into definitive endoderm cells using only baseline (Day 0) RNA-seq gene expression data.

A core bottleneck in iPSC-based cell therapy development is donor selection. Differentiation timelines are long, costs are high, and donor variability is significant. Single-cell RNA-seq data was aggregated to donor-level bulk expression, two independent differentiation targets were engineered (pseudorank and DE score), and multiple feature representations were evaluated (PCA, pathway scores, gene-level). This project demonstrates that a small set of ~20 genes is sufficient to accurately rank donor differentiation potential and correctly identify up to 4 of the top 5 donors. The final model uses CatBoost with SHAP-based automated feature selection.

**Key tools:** Python, ScanPy, CatBoost, SHAP, Scikit-learn, Pandas

---
### 🏥 [Modelling Hospital Length of Stay](./Modelling_Hospital_LoS)
**Capstone 1: Springboard Data Science Certification**

Predicting a patient's length of stay (LoS) at the time of admission would allow hospitals to more effectively schedule staffing, bed allocation, and resource planning. This project builds a regression model to predict LoS using vital signs and medical history from a dataset of 100,000 patients.

EDA revealed that most numeric features (hematocrit, creatinine, BMI, pulse, etc.) show a distinctive non-linear relationship with LoSm with extreme values often associated with *shorter* stays.  This pointed toward tree-based models as the right approach. An engineered feature summing total patient complications improved model performance. After screening seven algorithms, CatBoost with default settings outperformed all others, particularly for longer admissions (10+ days), which are the highest priority from a resource-planning perspective. The final model requires only 11 features and predicts stay length with a mean error of ±0.27 days.

**Key tools:** Python, Scikit-learn, CatBoost, XGBoost, Pandas, Matplotlib

---
### 🏥 [Modelling User Engagment to Identify Features of Active Users](./Mock_Interview_Data_Science_Challenges)
**Mock Interview Challenges: Springboard Data Science Certification**

As part of our final evaluation for the Data Science Certification, we were given several assignments designed to mimic data science challenges that might be posed to us during technical interviews.  Here I have included three projects to demonstrate my data visualization and modelling skills on the types of datasets found outside health care and biotech.  All three of these projects use simulated user data with the purpose of mimicking real world  businesses.

#### [Website User Logins](./Mock_Interview_Data_Science_Challenges/Website_logins)
Using timestamps from user logins, I use time series analysis to visualize and statistically analyze the patterns in website usage with the purpose of making business related recommendations to the company.

#### [Rideshare User Feature Evaluation](./Mock_Interview_Data_Science_Challenges/Rideshare_Active_User_Identification)
I used data on the rides booked from a rideshare company to identify and engineer features of active users with the purpose of making marketing recommendations to the company.

#### [Relax Data Science Challenge](./Mock_Interview_Data_Science_Challenges/Relax_Data_Science_Challenge)
In this challenge, I used two dataset describing users of an unknown business. One dataset contained metadata on the users, and the other dataset contained user logins.  In this project, I used time series analysis to define active users, then used predictive modelling with the metadata to find the features that characterized active users.  The findings were described in a report along with marketing recommendations for the client. 

**Key tools:** Python, Time Series, Scikit-learn, SHAP, CatBoost, Random Forest, XGBoost, Pandas, Matplotlib

---
### 🐴 [Horse Organizer](./Horse_Organizer)
**Final project for CS50P: Introduction to Python (Harvard University)**

A command-line tool for managing a list of sale horses in the sport of eventing. Users can search available horses by budget, competition level, and age range, add new horses to the roster, or remove sold horses with automatic timestamped backups before any edits.

The project emphasizes robust input handling: budget, age, and level inputs accept a wide range of natural language formats (e.g. "twenty-five thousand dollars", "eight to ten years old") using regex parsing and word-to-number conversion. Search results are ranked into Tier I matches (all criteria met) and Tier II matches (budget plus one other criterion).

**Key tools:** Python, CSV, Regex, w2n

---
## About This Portfolio

These projects represent the range of my data science work to date, from foundational Python development to applied machine learning on real biological datasets. Each project folder contains its own detailed README with methods, results, and code.

I'm actively looking for data science roles at the intersection of biology and machine learning. If something here resonates with challenges you're working on, I'd love to connect.

📫 [LinkedIn](https://www.linkedin.com/in/devon-svoboda-82b03421/)
