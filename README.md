# Telecom Customer Churn Analysis 📊

An interactive data analysis and visualization project based on the **Telco Customer Churn dataset**.  
The project analyzes customer behavior, identifies major churn patterns, and presents the findings through an interactive **Plotly Dash dashboard**.

---

## 📌 Project Overview

Customer churn is an important business problem for telecommunication companies because losing existing customers can directly affect revenue and growth.

This project focuses on analyzing customer data to understand:

- How many customers are active and how many have churned
- Which contract types have higher churn
- Whether monthly charges are related to churn
- Which internet services have higher churn
- How customer tenure affects retention
- Which customer segments require better retention strategies

The analysis combines data preprocessing, feature engineering, exploratory data analysis, business insights, and interactive visualization.

---

## 🎯 Objectives

The main objectives of this project are:

1. Understand the telecom customer dataset.
2. Clean and preprocess the data.
3. Handle missing values and identify data quality issues.
4. Create useful features for customer segmentation and analysis.
5. Perform exploratory data analysis using Python.
6. Identify important factors associated with customer churn.
7. Build an interactive Plotly Dash dashboard.
8. Provide business recommendations to improve customer retention.

---

## 📂 Dataset

The project uses the **Telco Customer Churn dataset** from Kaggle.

### Dataset Details

- **Records:** 7,043 customers
- **Features:** 21 original columns
- **Target Variable:** `Churn`

Important attributes include:

- Customer ID
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Churn

---

## 🧹 Data Preprocessing

The dataset was inspected and cleaned before performing the analysis.

Major preprocessing steps included:

- Checking the dataset structure and data types
- Checking for missing values
- Checking for duplicate records
- Converting `TotalCharges` into numeric format
- Handling missing values in `TotalCharges`
- Verifying categorical values
- Preparing the dataset for visualization and analysis

---

## ⚙️ Feature Engineering

Additional features were created to make the analysis more meaningful.

### Churn Numeric

The original `Churn` column contains `Yes` and `No` values.  
An additional numerical column was created:

- `No` → 0
- `Yes` → 1

### Monthly Charges Category

Customers were grouped according to their monthly spending:

- Low Spending
- Moderate Spending
- High Spending

### Customer Type

Customers were segmented according to their tenure:

- New Customer
- Regular Customer
- Loyal Customer

### Contract Rank

Contract types were also assigned an order based on their duration:

- Month-to-month → 1
- One year → 2
- Two year → 3

---

## 📊 Exploratory Data Analysis

Different visualizations were used to understand customer behavior and churn patterns.

The analysis included:

- Histogram
- KDE Plot
- Box Plot
- Violin Plot
- Count Plot
- Bar Plot
- Scatter Plot
- Regression Plot
- Correlation Heatmap
- Pair Plot

These visualizations helped identify trends, relationships, differences between customer groups, and possible factors influencing churn.

---

## 📈 Interactive Dashboard

The final dashboard was developed using **Plotly Dash**.

### Dashboard Features

#### KPI Cards

The dashboard displays:

- **Total Customers:** 7,043
- **Active Customers:** 5,174
- **Churned Customers:** 1,869
- **Churn Rate:** 26.54%

#### Interactive Filters

Users can filter the dashboard using:

- Gender
- Contract Type
- Internet Service

#### Dashboard Charts

The dashboard contains:

- Churn by Contract Type
- Churn by Internet Service
- Monthly Charges Distribution
- Customer Tenure Analysis
- Correlation Heatmap

The graphs support interactive exploration such as hovering, zooming, and filtering.

---

## 💡 Key Business Insights

The analysis highlighted several important customer retention patterns:

1. **Month-to-month contract customers show higher churn** compared with customers on longer-term contracts.

2. **Customers with shorter tenure are more likely to churn**, indicating that the early customer experience is important for retention.

3. **Higher monthly charges can be associated with increased churn**, suggesting that pricing and perceived value should be monitored.

4. **Fiber optic customers show a relatively higher churn pattern** compared with some other internet service groups.

5. **Electronic check users show higher churn**, making payment method an area worth investigating.

6. **Long-term contract customers tend to remain with the company longer**, showing the value of contract-based retention strategies.

7. **Customer tenure and total charges are positively related**, as customers who stay longer generally generate more cumulative revenue.

8. Customers using additional services such as **Online Security and Tech Support** can represent opportunities for better retention and service bundling.

---

## 💼 Business Recommendations

Based on the analysis, the following strategies can help improve customer retention:

### 1. Encourage Long-Term Contracts
Provide attractive discounts or benefits to month-to-month customers to encourage one-year or two-year contracts.

### 2. Focus on New Customers
Introduce better onboarding programs, welcome offers, and early engagement campaigns for new customers.

### 3. Review High Monthly Charges
Offer personalized plans or bundles to customers with high monthly charges so that they feel they are receiving sufficient value.

### 4. Improve Support Services
Promote services such as technical support and online security as part of retention-focused packages.

### 5. Review Payment Experience
Investigate the higher churn associated with electronic check payments and encourage convenient and reliable digital payment methods.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Plotly**
- **Plotly Dash**
- **Jupyter Notebook**
- **Git & GitHub**
- **Vercel**

---

## 📁 Project Structure

```text
Telecom-customer-churn/
│
├── app.py
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── requirements.txt
├── pyproject.toml
├── README.md
├── documentation.pdf
├── api/
│   └── index.py
└── .gitignore

## 🌐 Live Dashboard

[Open the Live Dashboard](https://telecom-customer-churn-analysis-gtyv6iqq6.vercel.app/)

## 📄 Project Documentation

[View Project Documentation](https://github.com/nidhi-1501/telecom-customer-churn-analysis/blob/main/Telecom%20Customer%20Churn%20Analysis%20Project%20Report.pdf)