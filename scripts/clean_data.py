import pandas as pd
import mysql.connector

# 1. Load data from MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bank_marketing'
)

query = "SELECT * FROM bank_data"
df = pd.read_sql(query, conn)

# 2. Rename 'default' column if needed (MySQL reserved keyword)
df.rename(columns={'default_status': 'default'}, inplace=True)

# 3. Check basic structure
print("\n🔹 Shape of data:", df.shape)
print("\n🔹 Data types:\n", df.dtypes)

# 4. Check for missing values
print("\n🔹 Missing values:\n", df.isnull().sum())

# 5. Standardize categorical fields (trim spaces, lowercase)
cat_cols = ['job', 'marital', 'education', 'default',
            'housing', 'loan', 'contact', 'month', 'poutcome', 'y']

for col in cat_cols:
    df[col] = df[col].str.strip().str.lower()

# 6. Convert 'yes'/'no' fields to binary
binary_map = {'yes': 1, 'no': 0}
df['default'] = df['default'].map(binary_map)
df['housing'] = df['housing'].map(binary_map)
df['loan'] = df['loan'].map(binary_map)
df['y'] = df['y'].map(binary_map)

# 7. Identify and handle outliers (optional - here we just flag them)
outliers = df[df['balance'] < -1000]
print("\n🔹 Potential outliers (balance < -1000):\n", outliers)

# 8. Save cleaned data for next step
df.to_csv("data/cleaned_bank_data.csv", index=False)
print("\n✅ Cleaned data saved to: data/cleaned_bank_data.csv")
