# Prompt Engineering Used for Synthetic Data Generation

## Objective

Generate realistic synthetic Uber Eats marketplace data for an end-to-end machine learning project.

The generated data must support:

- Customer segmentation
- Restaurant segmentation
- Sentiment analysis
- Delivery time prediction
- Tip prediction
- Hourly demand forecasting

---

## P.T.C.F. Prompt

### Persona

Act as a senior Python data engineer and machine learning data scientist.

### Task

Create a Python script using Pandas and NumPy to generate realistic synthetic Uber Eats marketplace datasets.

### Context

The datasets will be used for customer segmentation, restaurant segmentation, NLP sentiment analysis, regression and time-series forecasting.

### Format

Return clean Python code that creates CSV files.

The output should contain seven datasets:

1. Customers
2. Restaurants
3. Orders
4. Deliveries
5. Drivers
6. Reviews
7. Payments

The datasets must maintain valid relationships between their IDs.

---

## Role-Based Prompt

Act as a senior data engineer responsible for creating a realistic synthetic food-delivery marketplace dataset.

The data should contain realistic relationships between:

- Traffic and delivery time
- Delivery distance and delivery time
- Restaurant preparation time and delivery time
- Order amount and tip amount
- Customer rating and review sentiment
- Order timestamp and demand patterns

Generate Python code using Pandas and NumPy.

---

## Few-Shot Prompt

Example relationship:

Input:
Traffic = High
Distance = 12 km
Preparation Time = 30 minutes

Expected behavior:
Delivery time should generally be higher than an order with low traffic, short distance and low preparation time.

Example:

Rating = 5

Expected review sentiment:
Positive

Rating = 1

Expected review sentiment:
Negative

---

## Structured Output Requirements

Generate:

- customers.csv
- restaurants.csv
- orders.csv
- deliveries.csv
- drivers.csv
- reviews.csv
- payments.csv

The script should save all files into:

data/raw/

The script should also print the shape of every generated dataset.