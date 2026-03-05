import pandas as pd

data = {
    'order_id': [101, 102, 101, 103, 104, 102, 105],
    'product':  ['Apple', 'Banana', 'Apple', 'Cherry', 'Banana', 'Banana', 'Cherry'],
    'region':   ['North', 'South', 'North', 'East', 'South', 'South', 'West'],
    'sales':    [250, 150, 250, 300, 150, 150, 200]
}
df = pd.DataFrame(data)

# Remove duplicates
remove_duplicate = df.drop_duplicates(subset=['order_id'])

# Sort by sales descending
sorted_data = remove_duplicate.sort_values(['sales'], ascending=False)
print(sorted_data)

# Total sales per product 
product_groupby = remove_duplicate.groupby("product")
total_sales = product_groupby["sales"].sum()
print(total_sales)

# Avg sales per region, sorted descending 
region_groupby = remove_duplicate.groupby("region")
avg_sales = region_groupby["sales"].mean()
sorted_value = avg_sales.sort_values(ascending=False)
print(sorted_value)