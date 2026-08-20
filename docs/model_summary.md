# Uber Eats ML Model Summary

## 1. Customer Segmentation

### Models Used

* K-Means
* DBSCAN
* PCA for visualization

### Result

K-Means identified three major customer segments:

| Segment                          | Customers | Total Orders | Average Spending |
| -------------------------------- | --------: | -----------: | ---------------: |
| Regular Moderate-Value Customers |       413 |        1,760 |           893.08 |
| Premium Frequent Diners          |       314 |        2,393 |         1,693.74 |
| Occasional Low-Spend Customers   |       265 |          847 |           677.59 |

### Business Result

Premium Frequent Diners were identified as the most valuable and highest-volume customer segment.

---

## 2. Sentiment Analysis

### Techniques Used

* Text preprocessing
* Tokenization
* Stop-word removal
* Lemmatization
* TF-IDF
* Naive Bayes
* VADER

### Dataset

5,000 customer reviews.

### Sentiment Distribution

| Sentiment | Count | Percentage |
| --------- | ----: | ---------: |
| Neutral   | 2,040 |     40.80% |
| Positive  | 1,867 |     37.34% |
| Negative  | 1,093 |     21.86% |

### Business Result

21.86% of reviews were classified as negative, indicating an opportunity to investigate recurring causes of customer dissatisfaction.

---

## 3. Delivery Time Prediction

### Target

`delivery_time_minutes`

### Features

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

### Models

* Linear Regression
* Random Forest Regression

### Operational Findings

| Condition      | Average Delivery Time |
| -------------- | --------------------: |
| Low Traffic    |             55.66 min |
| Medium Traffic |             62.59 min |
| High Traffic   |             73.30 min |
| Clear Weather  |             60.67 min |
| Heavy Rain     |             74.28 min |

High traffic was associated with approximately 17.64 additional minutes compared with low traffic.

Heavy rain was associated with approximately 13.62 additional minutes compared with clear weather.

---

## 4. Demand Forecasting

### Time-Series Preparation

* Hourly order aggregation
* Trend analysis
* Seasonality analysis
* Time-series decomposition
* ADF stationarity test
* Chronological train/test split

### Models

* ARIMA
* Prophet

### Evaluation

| Model   |    MAE |   RMSE |
| ------- | -----: | -----: |
| ARIMA   | 0.7946 | 1.0753 |
| Prophet | 0.7925 | 1.0795 |

### Model Selection

* Best MAE: Prophet
* Best RMSE: ARIMA

ARIMA was selected as the final forecasting model based on RMSE.

### Forecast

The final 24-hour forecast predicts approximately 1.08 orders/hour with very little variation.

The current forecast does not indicate a significant demand spike.

---

## 5. Overall Business Impact

The combined system provides four major capabilities:

### Customer Intelligence

Identify valuable customer segments and prioritize retention strategies.

### Customer Experience

Identify negative customer sentiment and investigate recurring complaints.

### Operational Intelligence

Identify traffic and weather conditions associated with longer delivery times.

### Demand Planning

Forecast short-term order demand to support operational capacity planning.

---

## 6. Model Limitations

* The project uses synthetic data.
* Customer clusters depend on selected features and clustering assumptions.
* Traditional TF-IDF models have limited contextual understanding.
* Delivery predictions depend on the available operational features.
* Demand forecasting is limited by relatively stable demand in the synthetic dataset.
* Real-world holidays, promotions, events, locations, and external factors are not fully represented.

---

## 7. Future Improvements

* Use real-world historical Uber Eats-style data.
* Apply BERT/Transformer models for contextual sentiment analysis.
* Add location-level and driver-level delivery features.
* Include holidays, promotions, events, and stronger seasonal patterns.
* Perform location-level demand forecasting.
* Deploy models through an API or Streamlit application.
* Implement automated model monitoring and retraining.
