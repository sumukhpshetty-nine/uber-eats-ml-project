import os
import random
import numpy as np
import pandas as pd


# ============================================================
# 1. CONFIGURATION
# ============================================================

SEED = 42

np.random.seed(SEED)
random.seed(SEED)

OUTPUT_DIR = "data/raw"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# Number of records
N_CUSTOMERS = 1000
N_RESTAURANTS = 100
N_ORDERS = 5000
N_DRIVERS = 500


# ============================================================
# 2. HELPER FUNCTIONS
# ============================================================

def random_dates(start_date, end_date, n):
    """
    Generate random timestamps between two dates.
    """
    start = pd.Timestamp(start_date)
    end = pd.Timestamp(end_date)

    random_seconds = np.random.randint(
        0,
        int((end - start).total_seconds()),
        n
    )

    return start + pd.to_timedelta(random_seconds, unit="s")


# ============================================================
# 3. CUSTOMERS
# ============================================================

customer_ids = [
    f"CUST_{i:04d}"
    for i in range(1, N_CUSTOMERS + 1)
]

customers = pd.DataFrame({
    "customer_id": customer_ids,

    "age": np.random.randint(
        18,
        65,
        N_CUSTOMERS
    ),

    "gender": np.random.choice(
        ["Male", "Female", "Other"],
        N_CUSTOMERS,
        p=[0.48, 0.48, 0.04]
    ),

    "city": np.random.choice(
        [
            "Bengaluru",
            "Mumbai",
            "Delhi",
            "Hyderabad",
            "Chennai",
            "Pune"
        ],
        N_CUSTOMERS
    ),

    "signup_date": random_dates(
        "2024-01-01",
        "2026-01-01",
        N_CUSTOMERS
    ),

    "membership_type": np.random.choice(
        [
            "Regular",
            "Premium"
        ],
        N_CUSTOMERS,
        p=[0.75, 0.25]
    )
})


# ============================================================
# 4. RESTAURANTS
# ============================================================

restaurant_ids = [
    f"REST_{i:03d}"
    for i in range(1, N_RESTAURANTS + 1)
]

restaurant_categories = [
    "Indian",
    "Chinese",
    "Fast Food",
    "Pizza",
    "Biryani",
    "South Indian",
    "North Indian",
    "Cafe",
    "Desserts",
    "Healthy"
]

restaurants = pd.DataFrame({
    "restaurant_id": restaurant_ids,

    "restaurant_name": [
        f"Restaurant_{i:03d}"
        for i in range(1, N_RESTAURANTS + 1)
    ],

    "category": np.random.choice(
        restaurant_categories,
        N_RESTAURANTS
    ),

    "city": np.random.choice(
        [
            "Bengaluru",
            "Mumbai",
            "Delhi",
            "Hyderabad",
            "Chennai",
            "Pune"
        ],
        N_RESTAURANTS
    ),

    "rating": np.round(
        np.clip(
            np.random.normal(4.1, 0.5, N_RESTAURANTS),
            2.5,
            5.0
        ),
        1
    ),

    "avg_preparation_time": np.random.randint(
        10,
        41,
        N_RESTAURANTS
    )
})


# ============================================================
# 5. DRIVERS
# ============================================================

driver_ids = [
    f"DRV_{i:04d}"
    for i in range(1, N_DRIVERS + 1)
]

drivers = pd.DataFrame({
    "driver_id": driver_ids,

    "age": np.random.randint(
        20,
        55,
        N_DRIVERS
    ),

    "vehicle_type": np.random.choice(
        [
            "Bike",
            "Scooter",
            "Car"
        ],
        N_DRIVERS,
        p=[0.45, 0.40, 0.15]
    ),

    "rating": np.round(
        np.clip(
            np.random.normal(4.3, 0.4, N_DRIVERS),
            2.5,
            5.0
        ),
        1
    ),

    "experience_years": np.random.randint(
        1,
        10,
        N_DRIVERS
    )
})


# ============================================================
# 6. ORDERS
# ============================================================

order_ids = [
    f"ORD_{i:05d}"
    for i in range(1, N_ORDERS + 1)
]

order_customer_ids = np.random.choice(
    customer_ids,
    N_ORDERS
)

order_restaurant_ids = np.random.choice(
    restaurant_ids,
    N_ORDERS
)

order_timestamps = random_dates(
    "2026-01-01",
    "2026-07-01",
    N_ORDERS
)

number_of_items = np.random.randint(
    1,
    7,
    N_ORDERS
)

order_amount = np.round(
    np.random.lognormal(
        mean=5.2,
        sigma=0.55,
        size=N_ORDERS
    ),
    2
)

order_amount = np.clip(
    order_amount,
    100,
    2500
)

weather = np.random.choice(
    [
        "Clear",
        "Cloudy",
        "Rain",
        "Heavy Rain"
    ],
    N_ORDERS,
    p=[0.50, 0.25, 0.20, 0.05]
)

traffic = np.random.choice(
    [
        "Low",
        "Medium",
        "High"
    ],
    N_ORDERS,
    p=[0.30, 0.45, 0.25]
)

order_status = np.random.choice(
    [
        "Delivered",
        "Cancelled"
    ],
    N_ORDERS,
    p=[0.93, 0.07]
)

orders = pd.DataFrame({
    "order_id": order_ids,

    "customer_id": order_customer_ids,

    "restaurant_id": order_restaurant_ids,

    "order_timestamp": order_timestamps,

    "order_amount": order_amount,

    "number_of_items": number_of_items,

    "weather": weather,

    "traffic_condition": traffic,

    "order_status": order_status
})


# ============================================================
# 7. RESTAURANT PREPARATION TIME
# ============================================================

restaurant_prep_map = restaurants.set_index(
    "restaurant_id"
)["avg_preparation_time"]

orders["preparation_time_minutes"] = (
    orders["restaurant_id"]
    .map(restaurant_prep_map)
    .astype(float)
)

orders["preparation_time_minutes"] += np.random.randint(
    -5,
    6,
    N_ORDERS
)

orders["preparation_time_minutes"] = np.clip(
    orders["preparation_time_minutes"],
    5,
    60
)


# ============================================================
# 8. DELIVERIES
# ============================================================

delivery_ids = [
    f"DEL_{i:05d}"
    for i in range(1, N_ORDERS + 1)
]

delivery_driver_ids = np.random.choice(
    driver_ids,
    N_ORDERS
)

delivery_distance = np.round(
    np.random.gamma(
        shape=2.5,
        scale=2.0,
        size=N_ORDERS
    ),
    2
)

delivery_distance = np.clip(
    delivery_distance,
    0.5,
    20
)


# Convert categorical traffic/weather into numerical effects
traffic_effect = orders["traffic_condition"].map({
    "Low": 0,
    "Medium": 8,
    "High": 18
})

weather_effect = orders["weather"].map({
    "Clear": 0,
    "Cloudy": 3,
    "Rain": 8,
    "Heavy Rain": 15
})


# Time of day effect
order_hour = orders["order_timestamp"].dt.hour

rush_hour_effect = np.where(
    order_hour.isin([12, 13, 14, 19, 20, 21]),
    10,
    0
)


# Delivery time formula
delivery_time = (
    10
    + delivery_distance * 4
    + orders["preparation_time_minutes"] * 0.8
    + traffic_effect
    + weather_effect
    + rush_hour_effect
    + np.random.normal(0, 5, N_ORDERS)
)

delivery_time = np.round(
    np.clip(
        delivery_time,
        15,
        150
    ),
    1
)


# ============================================================
# 9. TIP AMOUNT
# ============================================================

tip_amount = (
    order_amount * np.random.uniform(
        0.02,
        0.15,
        N_ORDERS
    )
)

tip_amount += np.random.normal(
    10,
    5,
    N_ORDERS
)

tip_amount = np.round(
    np.clip(
        tip_amount,
        0,
        300
    ),
    2
)


deliveries = pd.DataFrame({
    "delivery_id": delivery_ids,

    "order_id": order_ids,

    "driver_id": delivery_driver_ids,

    "delivery_distance_km": delivery_distance,

    "preparation_time_minutes": orders[
        "preparation_time_minutes"
    ],

    "delivery_time_minutes": delivery_time,

    "tip_amount": tip_amount
})


# ============================================================
# 10. REVIEWS
# ============================================================

review_ids = [
    f"REV_{i:05d}"
    for i in range(1, N_ORDERS + 1)
]


# Rating influenced by delivery experience
rating_base = np.where(
    delivery_time <= 35,
    4.5,
    np.where(
        delivery_time <= 55,
        4.0,
        np.where(
            delivery_time <= 80,
            3.0,
            2.0
        )
    )
)

ratings = np.round(
    np.clip(
        rating_base + np.random.normal(0, 0.5, N_ORDERS),
        1,
        5
    )
)

ratings = ratings.astype(int)


def generate_review(rating, traffic_condition, weather_condition):
    """
    Generate a simple review based on order experience.
    """

    if rating >= 4:
        positive_reviews = [
            "Food was delicious and delivery was fast.",
            "Great food and excellent service.",
            "Amazing experience, food arrived hot.",
            "Very good service and tasty food.",
            "Loved the food and quick delivery."
        ]

        return random.choice(positive_reviews)

    elif rating == 3:
        neutral_reviews = [
            "Food was okay but delivery took some time.",
            "Average experience.",
            "Food was decent but could be better.",
            "Delivery was acceptable.",
            "The experience was okay."
        ]

        return random.choice(neutral_reviews)

    else:
        negative_reviews = [
            "Delivery was very late and food was cold.",
            "Food arrived late.",
            "Very slow delivery and poor experience.",
            "Order was delayed and food was not hot.",
            "The delivery took too long."
        ]

        return random.choice(negative_reviews)


review_text = [
    generate_review(
        ratings[i],
        orders.loc[i, "traffic_condition"],
        orders.loc[i, "weather"]
    )
    for i in range(N_ORDERS)
]


reviews = pd.DataFrame({
    "review_id": review_ids,

    "order_id": order_ids,

    "customer_id": order_customer_ids,

    "rating": ratings,

    "review_text": review_text
})


# ============================================================
# 11. PAYMENTS
# ============================================================

payment_ids = [
    f"PAY_{i:05d}"
    for i in range(1, N_ORDERS + 1)
]

payments = pd.DataFrame({
    "payment_id": payment_ids,

    "order_id": order_ids,

    "payment_method": np.random.choice(
        [
            "UPI",
            "Credit Card",
            "Debit Card",
            "Cash"
        ],
        N_ORDERS,
        p=[0.50, 0.20, 0.20, 0.10]
    ),

    "payment_amount": np.round(
        orders["order_amount"] + tip_amount,
        2
    )
})


# ============================================================
# 12. SAVE DATASETS
# ============================================================

customers.to_csv(
    f"{OUTPUT_DIR}/customers.csv",
    index=False
)

restaurants.to_csv(
    f"{OUTPUT_DIR}/restaurants.csv",
    index=False
)

orders.to_csv(
    f"{OUTPUT_DIR}/orders.csv",
    index=False
)

deliveries.to_csv(
    f"{OUTPUT_DIR}/deliveries.csv",
    index=False
)

drivers.to_csv(
    f"{OUTPUT_DIR}/drivers.csv",
    index=False
)

reviews.to_csv(
    f"{OUTPUT_DIR}/reviews.csv",
    index=False
)

payments.to_csv(
    f"{OUTPUT_DIR}/payments.csv",
    index=False
)


# ============================================================
# 13. VALIDATION OUTPUT
# ============================================================

print("\n" + "=" * 60)
print("SYNTHETIC DATA GENERATION COMPLETE")
print("=" * 60)

print("\nDataset Shapes:")

print("Customers   :", customers.shape)
print("Restaurants :", restaurants.shape)
print("Orders      :", orders.shape)
print("Deliveries  :", deliveries.shape)
print("Drivers     :", drivers.shape)
print("Reviews     :", reviews.shape)
print("Payments    :", payments.shape)

print("\nFiles saved to:")
print(OUTPUT_DIR)

print("\n" + "=" * 60)