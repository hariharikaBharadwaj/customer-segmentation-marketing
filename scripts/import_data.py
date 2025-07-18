import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bank_marketing'
)

# SQL query
query = "SELECT * FROM bank_data"

# Load into pandas
df = pd.read_sql(query, conn)

# Preview
print(df.head())
