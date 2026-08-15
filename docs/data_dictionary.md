# Uber Eats Synthetic Dataset – Data Dictionary

## Customers

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| age | Customer age |
| gender | Customer gender |
| city | Customer city |
| signup_date | Date the customer registered |
| membership_type | Customer membership type |

## Restaurants

| Column | Description |
|---|---|
| restaurant_id | Unique restaurant identifier |
| restaurant_name | Restaurant name |
| category | Restaurant food category |
| city | Restaurant city |
| rating | Restaurant rating |
| avg_preparation_time | Average food preparation time in minutes |

## Orders

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer_id | Customer who placed the order |
| restaurant_id | Restaurant receiving the order |
| order_timestamp | Date and time of the order |
| order_amount | Total order amount |
| number_of_items | Number of items in the order |
| weather | Weather condition |
| traffic_condition | Traffic condition |
| order_status | Status of the order |
| preparation_time_minutes | Food preparation time |

## Deliveries

| Column | Description |
|---|---|
| delivery_id | Unique delivery identifier |
| order_id | Related order |
| driver_id | Driver assigned to the order |
| delivery_distance_km | Delivery distance in kilometres |
| preparation_time_minutes | Food preparation time |
| delivery_time_minutes | Total delivery time |
| tip_amount | Tip given by customer |

## Drivers

| Column | Description |
|---|---|
| driver_id | Unique driver identifier |
| age | Driver age |
| vehicle_type | Driver vehicle type |
| rating | Driver rating |
| experience_years | Driver experience |

## Reviews

| Column | Description |
|---|---|
| review_id | Unique review identifier |
| order_id | Related order |
| customer_id | Customer who submitted the review |
| rating | Customer rating from 1 to 5 |
| review_text | Customer written feedback |

## Payments

| Column | Description |
|---|---|
| payment_id | Unique payment identifier |
| order_id | Related order |
| payment_method | Payment method used |
| payment_amount | Total payment amount |