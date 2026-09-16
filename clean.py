import pandas as pd

df = pd.read_csv('tech_sales_raw.csv')

df = df.drop_duplicates()

df['Country'] = df['Country'].str.strip()
df['Country'] = df['Country'].str.title()

df['Category'] = df['Category'].str.strip()
df['Category'] = df['Category'].str.title()

df['Product'] = df['Product'].str.strip()

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

df['Order Date'] = df['Order Date'].fillna(pd.to_datetime('2023-05-15'))
df['Ship Date'] = df['Ship Date'].fillna(pd.to_datetime('2023-05-18'))

df['Profit ($)'] = df['Revenue ($)'] - df['Cost ($)']
df['Profit Margin %'] = (df['Profit ($)'] / df['Revenue ($)']) * 100

df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Month Name'] = df['Order Date'].dt.strftime('%b')

df.to_csv('tech_sales_cleaned.csv', index=False)