import pandas as pd

df = pd.read_csv("data/transactions.csv", parse_dates=['timestamp'])

# time feature
df['hour'] = df['timestamp'].dt.hour

# user transaction count
df['user_txn_count'] = df.groupby('user_id')['transaction_id'].transform('count')

# average spending
df['user_avg_amt'] = df.groupby('user_id')['amount'].transform('mean')

# spending deviation
df['amt_deviation'] = df['amount'] - df['user_avg_amt']

# device sharing indicator
df['device_usage'] = df.groupby('device_id')['user_id'].transform('count')

# 🚨 transaction velocity (important)
df['txn_per_hour'] = df.groupby(['user_id','hour'])['transaction_id'].transform('count')

# location change flag
df['location_change'] = (
    df['location'] != df.groupby('user_id')['location'].transform('first')
).astype(int)

df.to_csv("data/featured_transactions.csv", index=False)

print("✅ Features created: data/featured_transactions.csv")