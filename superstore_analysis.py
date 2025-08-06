import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='ISO-8859-1')

# 2. Preview Dataset
print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())

# 3. Check for Missing Values
print("\nMissing Values:\n", df.isnull().sum())

# 4. Check for Duplicates
print("\nDuplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# 5. Convert Dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 6. Clean Columns (e.g., Strip whitespace)
df.columns = df.columns.str.strip()

# 7. Save Cleaned File
df.to_csv("cleaned_superstore.csv", index=False)
print("Cleaned data saved.")