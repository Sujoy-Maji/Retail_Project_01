import pandas as pd

# 1. Load the raw data
df = pd.read_csv('raw_retail_sales.csv')

# 2. Fix the dates to a standard format (YYYY-MM-DD)
df['date'] = pd.to_datetime(df['date'], format='mixed').dt.strftime('%Y-%m-%d')

# 3. Fill missing numbers (put 1 for missing quantity, 0 for missing price)
df['quantity'] = df['quantity'].fillna(1)
df['price'] = df['price'].fillna(0)

# 4. Fill missing text (put 'Unknown' for missing product or location)
df['product'] = df['product'].fillna('Unknown')
df['store_location'] = df['store_location'].fillna('Unknown')

# 5. Remove any exact duplicate rows
df = df.drop_duplicates()

# 6. Save the clean data to a new file
df.to_csv('cleaned_retail_sales.csv', index=False)
print("Data cleaning successful! Clean file saved.")
