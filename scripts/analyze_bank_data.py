
# Jupyter Notebook: Stored Procedure Analysis for Cleaned Bank Marketing Data

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',  # ✅ Use the password that works in terminal
    'database': 'bank_marketing'
}


# Function to call stored procedure and return DataFrame
def fetch_proc_results(proc_name):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.callproc(proc_name)
    for result in cursor.stored_results():
        cols = [col[0] for col in result.description]
        df = pd.DataFrame(result.fetchall(), columns=cols)
        return df
    cursor.close()
    conn.close()

# Call stored procedures
df_edu = fetch_proc_results('GetSubscriptionByEducation')
df_job = fetch_proc_results('GetAvgBalanceByJob')
df_age = fetch_proc_results('GetSubscriptionByAgeGroup')

# Plot the results
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

# 1. Education vs Subscribed
axs[0].bar(df_edu['education'], df_edu['subscribed'], color='seagreen')
axs[0].set_title('Subscribers by Education')
axs[0].tick_params(axis='x', rotation=45)

# 2. Avg Balance by Job
axs[1].barh(df_job['job'], df_job['avg_balance'], color='steelblue')
axs[1].set_title('Average Balance by Job')

# 3. Subscription Rate by Age Group
axs[2].bar(df_age['age_group'], df_age['subscription_rate_pct'], color='darkorange')
axs[2].set_title('Subscription Rate by Age Group')
axs[2].set_ylabel('% Subscribed')

plt.tight_layout()
plt.show()

print("🔹 df_edu:", df_edu.shape)
print("🔹 df_job:", df_job.shape)
print("🔹 df_age:", df_age.shape)

