# Uber Eats Operational & Customer Intelligence System

## Project Overview

This project builds an end-to-end machine learning and analytics system for a food delivery marketplace.

The objective is to use customer, restaurant, order, delivery, and review data to understand customer behavior, analyze customer sentiment, predict delivery times, forecast order demand, and translate model outputs into actionable business recommendations.

The project covers the complete ML workflow:

**Raw Data → Data Preparation → Feature Engineering → Modeling → Evaluation → Prediction → Business Insights**

---

## Business Problems

The system addresses four major business problems:

1. **Customer Segmentation**

   * Identify different customer behavior patterns.
   * Identify high-value customer segments.

2. **Customer Feedback Analysis**

   * Understand customer sentiment.
   * Identify negative customer experiences.

3. **Delivery Time Prediction**

   * Predict delivery time using operational and order-related features.
   * Identify factors associated with delivery delays.

4. **Hourly Demand Forecasting**

   * Forecast future order demand.
   * Support delivery capacity and operational planning.

---

## Dataset

The project uses synthetically generated Uber Eats-style marketplace data.

The raw datasets include:

* Customers
* Restaurants
* Orders
* Deliveries
* Drivers
* Payments
* Reviews

The generated dataset contains:

* 1,000 customers
* 100 restaurants
* 5,000 orders
* 5,000 deliveries
* 5,000 reviews

The data covers the period:

**January 1, 2026 – June 30, 2026**

---

## Project Components

### 1. Customer Segmentation

Techniques used:

* K-Means clustering
* DBSCAN
* PCA for cluster visualization and analysis
* StandardScaler

Customer behavior features included:

* Total orders
* Average order value
* Total spending
* Weekend orders
* Late-night orders
* Ordering frequency
* Average rating given

### Key Result

Three major customer segments were identified:

| Segment                          | Customers | Total Orders | Avg. Total Spending |
| -------------------------------- | --------: | -----------: | ------------------: |
| Regular Moderate-Value Customers |       413 |        1,760 |                 893 |
| Premium Frequent Diners          |       314 |        2,393 |               1,694 |
| Occasional Low-Spend Customers   |       265 |          847 |                 678 |

**Premium Frequent Diners** were identified as the most valuable and highest-volume customer segment.

---

## 2. Customer Feedback Analysis — NLP

The customer reviews were processed using:

* Lowercasing
* Tokenization
* Stop-word removal
* Lemmatization
* Punctuation removal
* TF-IDF vectorization

Sentiment classification was performed using:

* Naive Bayes
* VADER

### Sentiment Distribution

| Sentiment | Reviews | Percentage |
| --------- | ------: | ---------: |
| Neutral   |   2,040 |     40.80% |
| Positive  |   1,867 |     37.34% |
| Negative  |   1,093 |     21.86% |

Approximately **21.86% of customer reviews were classified as negative**, highlighting an opportunity to investigate recurring customer complaints.

---

## 3. Delivery Time Prediction

The selected regression objective was:

**Predict `delivery_time_minutes`**

Features included:

* Delivery distance
* Order amount
* Number of items
* Preparation time
* Traffic condition
* Weather
* Time of day
* Day of week
* Restaurant rating
* Restaurant category

The project evaluated regression approaches including:

* Linear Regression
* Random Forest Regression

### Key Operational Findings

Average delivery time by traffic:

| Traffic | Avg. Delivery Time |
| ------- | -----------------: |
| Low     |          55.66 min |
| Medium  |          62.59 min |
| High    |          73.30 min |

High traffic was associated with approximately **17.64 additional minutes** of delivery time compared with low traffic.

Average delivery time by weather:

| Weather    | Avg. Delivery Time |
| ---------- | -----------------: |
| Clear      |          60.67 min |
| Cloudy     |          63.01 min |
| Rain       |          67.80 min |
| Heavy Rain |          74.28 min |

Heavy rain was associated with approximately **13.62 additional minutes** compared with clear weather.

---

## 4. Hourly Demand Forecasting

Orders were aggregated into hourly demand.

The time-series workflow included:

* Hourly aggregation
* Hourly/daily pattern analysis
* Trend analysis
* Seasonality analysis
* Time-series decomposition
* Augmented Dickey-Fuller (ADF) test
* Chronological train/test split
* ARIMA
* Prophet

The dataset contained **4,344 hourly observations**.

### Stationarity

The ADF test indicated that the hourly demand series was stationary:

* ADF statistic: **-65.54**
* p-value: **0.0**

### Model Comparison

| Model   |   MAE |  RMSE |
| ------- | ----: | ----: |
| ARIMA   | 0.795 | 1.075 |
| Prophet | 0.793 | 1.079 |

Based on:

* **MAE:** Prophet performed slightly better.
* **RMSE:** ARIMA performed slightly better.

ARIMA was selected as the final forecasting model based on RMSE.

### Forecast Result

The final 24-hour forecast indicates relatively stable demand around:

**1.08 orders/hour**

The current forecast does not indicate a significant demand spike.

---

## Business Insights

The ML results provide several actionable insights.

### Customer Retention

Premium Frequent Diners generate the highest order volume and spending.

**Recommendation:** Prioritize loyalty programs, personalized offers, and retention initiatives for this segment.

### Traffic Management

High traffic is associated with approximately 17.64 additional minutes of delivery time compared with low traffic.

**Recommendation:** Increase rider availability and improve delivery allocation during high-traffic conditions.

### Weather Management

Heavy rain is associated with approximately 13.62 additional minutes of delivery time compared with clear weather.

**Recommendation:** Adjust delivery estimates and operational capacity during severe weather conditions.

### Customer Experience

21.86% of reviews were classified as negative.

**Recommendation:** Analyze recurring themes in negative reviews and address the operational causes of dissatisfaction.

### Demand Planning

The current 24-hour forecast indicates stable demand.

**Recommendation:** Maintain relatively stable delivery capacity rather than making large capacity changes based on the current forecast.

---

## Model Limitations

### Customer Segmentation

Cluster assignments depend on the selected features, scaling approach, and clustering assumptions.

### NLP

Traditional TF-IDF-based models may not fully understand:

* Context
* Sarcasm
* Complex language
* Semantic relationships

### Delivery Prediction

Prediction quality depends on the available operational features and the quality of the synthetic dataset.

### Demand Forecasting

The synthetic dataset has relatively low and stable hourly demand. Therefore, the current forecasting model has limited ability to demonstrate strong real-world demand spikes.

---

## Future Scope

Potential improvements include:

* Experimenting with additional customer and restaurant segmentation features.
* Using BERT/Transformer-based models for contextual sentiment analysis.
* Adding richer location, route, driver, and traffic features for delivery prediction.
* Using real-world historical demand data.
* Incorporating holidays, events, promotions, and stronger seasonal patterns into demand forecasting.
* Performing location-level demand forecasting.
* Deploying the models through an API or Streamlit application.
* Implementing automated model retraining and monitoring.

---

## Project Structure

```text
uber-eats-ml-capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_generation.ipynb
│   ├── 02_nlp_sentiment.ipynb
│   ├── 03_delivery_time_prediction.ipynb
│   ├── 04_demand_forecasting.ipynb
│   └── 05_end_to_end_pipeline.ipynb
│
├── src/
│
├── docs/
│   ├── data_dictionary.md
│   └── prompt.md
│
├── outputs/
│   ├── models/
│   ├── plots/
│   └── business insights/
│
├── data_generation.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* NLTK
* VADER
* Statsmodels
* XGBoost
* Prophet
* Jupyter Notebook
* Git/GitHub

---

## ML Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
├── Customer Segmentation
│      ├── K-Means
│      ├── DBSCAN
│      └── PCA
│
├── Sentiment Analysis
│      ├── Text Preprocessing
│      ├── TF-IDF
│      ├── Naive Bayes
│      └── VADER
│
├── Delivery Prediction
│      ├── Feature Engineering
│      ├── Regression
│      └── Evaluation
│
└── Demand Forecasting
       ├── Decomposition
       ├── ADF Test
       ├── ARIMA
       └── Prophet
              ↓
       Model Evaluation
              ↓
       Business Insights
              ↓
       Business Recommendations
```

---

## Reproducibility

The project uses a fixed random seed during synthetic data generation and stores processed datasets, trained models, evaluation results, and visualizations in the project structure.

The notebooks can be executed sequentially to reproduce the analysis and model outputs.
