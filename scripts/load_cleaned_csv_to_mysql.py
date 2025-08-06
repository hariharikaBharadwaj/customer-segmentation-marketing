
import pandas as pd
from sqlalchemy import create_engine

# Load the cleaned CSV
csv_path = "data/cleaned_bank_data.csv"  # Adjust if needed
df = pd.read_csv(csv_path)

# Create SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://root:Vijaya@123@localhost/da1")

# Load into MySQL (replace table if it exists)
df.to_sql(name='bank_data', con=engine, if_exists='replace', index=False)

print("✅ Data loaded into MySQL table 'da1.bank_data' successfully.")
