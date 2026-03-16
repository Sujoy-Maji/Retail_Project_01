import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 1. Generate 3,000 rows of professional retail data
print("Downloading enterprise dataset...")
np.random.seed(42)
products = {
    'MacBook Pro 16-inch': {'cat': 'Laptops', 'price': 2499.00},
    'AirPods Pro Gen 2': {'cat': 'Audio', 'price': 249.00},
    'Dell UltraSharp 27 Monitor': {'cat': 'Displays', 'price': 599.00},
    'Logitech MX Master 3S': {'cat': 'Peripherals', 'price': 99.00},
    'iPad Air 5th Gen': {'cat': 'Tablets', 'price': 599.00},
    'Sony WH-1000XM5': {'cat': 'Audio', 'price': 398.00}
}
locations = ['Bengaluru - Indiranagar', 'Mumbai - BKC', 'Delhi - Connaught Place', 'Hyderabad - HITEC City']

data = []
start_date = datetime(2025, 1, 1)
for i in range(3000):
    # Weight the hours so 5 PM - 8 PM is the peak
    hour = int(np.random.normal(17, 3))
    if hour > 23 or hour < 8: hour = 14
    
    date = start_date + timedelta(days=random.randint(0, 365), hours=hour, minutes=random.randint(0,59))
    prod_name = random.choice(list(products.keys()))
    
    data.append({
        'order_id': 10000 + i,
        'transaction_date': date.strftime('%Y-%m-%d %H:%M:%S'),
        'product_name': prod_name,
        'category': products[prod_name]['cat'],
        'quantity': random.choices([1, 2, 3], weights=[0.8, 0.15, 0.05])[0],
        'unit_price': products[prod_name]['price'],
        'store_location': random.choice(locations)
    })

df = pd.DataFrame(data)

# 2. Add some messy data for the script to clean
df.loc[10:25, 'unit_price'] = np.nan
df.loc[50:60, 'store_location'] = np.nan
df.to_csv('raw_retail_sales.csv', index=False)

# 3. Clean the data professionally
print("Cleaning data and extracting timestamps...")
df_clean = pd.read_csv('raw_retail_sales.csv')
df_clean['transaction_date'] = pd.to_datetime(df_clean['transaction_date'])
df_clean['hour_of_day'] = df_clean['transaction_date'].dt.hour
df_clean['month'] = df_clean['transaction_date'].dt.month_name()
df_clean['unit_price'] = df_clean.groupby('product_name')['unit_price'].transform(lambda x: x.fillna(x.mean()))
df_clean['store_location'] = df_clean['store_location'].fillna('Online Store (Website)')
df_clean['total_revenue'] = df_clean['quantity'] * df_clean['unit_price']

df_clean.to_csv('cleaned_retail_sales.csv', index=False)
print("Success! 3,000 rows of professional data saved.")
