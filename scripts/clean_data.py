
import pandas as pd
import mysql.connector
import os

# 1. Connect to MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='bank_marketing'
    )
    if conn.is_connected():
        print("✅ Connected to MySQL")
    else:
        raise Exception("❌ Failed to connect to MySQL")

    # 2. Load data from MySQL
    query = "SELECT * FROM bank_data"
    df = pd.read_sql(query, conn)

    if df.empty:
        raise ValueError("❌ The 'bank_data' table is empty.")

    # 3. Rename 'default' column if it exists
    if 'default' in df.columns:
        df.rename(columns={'default': 'default_status'}, inplace=True)

    # 4. Standardize categorical fields
    cat_cols = ['job', 'marital', 'education', 'default_status',
                'housing', 'loan', 'contact', 'month', 'poutcome', 'y']
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()

    # 5. Convert yes/no fields to binary
    binary_map = {'yes': 1, 'no': 0}
    for col in ['default_status', 'housing', 'loan', 'y']:
        if col in df.columns:
            df[col] = df[col].map(binary_map)

    # 6. Print y column distribution
    if 'y' in df.columns:
        print("🔍 Value counts for 'y':")
        print(df['y'].value_counts(dropna=False))

    # 7. Save cleaned CSV
    os.makedirs("data", exist_ok=True)
    save_path = os.path.abspath("data/cleaned_bank_data.csv")
    df.to_csv(save_path, index=False)
    print(f"✅ Cleaned data saved to: {save_path}")

except Exception as e:
    print("❌ ERROR:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔌 MySQL connection closed.")
