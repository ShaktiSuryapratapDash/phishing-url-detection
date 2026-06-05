import pandas as pd

# Load the dataset
df = pd.read_csv('PhishingData.csv')

# Display basic info
print("Shape of dataset:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Optional: show more rows
print("\nFirst 10 rows:")
print(df.head(10))