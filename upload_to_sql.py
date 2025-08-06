import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import os
from getpass import getpass

# Load cleaned dataset
df = pd.read_csv("cleaned_superstore.csv")
print(f"✅ DataFrame loaded with shape: {df.shape}")

# MySQL Workbench login - SECURE VERSION
username = "root"
# Get password securely (will prompt user)
raw_password = getpass("Enter MySQL password: ")
password = urllib.parse.quote_plus(raw_password)
host = "localhost"
port = "3306"
database = "superstore"

# Create MySQL connection engine
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Upload if DataFrame is not empty
if not df.empty:
    df.to_sql(name="superstore_orders", con=engine, if_exists="replace", index=False)
    print("✅ Data uploaded to MySQL table: superstore_orders")
else:
    print("❌ DataFrame is empty! Nothing uploaded.")
