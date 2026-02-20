import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

N = 10000
fraud_rate = 0.03

users = [f'U{i}' for i in range(500)]
merchants = [f'M{i}' for i in range(100)]
cities = ['Delhi','Mumbai','Bangalore','Kolkata','Chennai']
methods = ['UPI','Card','NetBanking','Wallet']

data = []
start_time = datetime(2024,1,1)

# store user home city
user_home_city = {user: random.choice(cities) for user in users}

for i in range(N):
    user = random.choice(users)
    merchant = random.choice(merchants)

    amount = round(np.random.exponential(2000),2)
    timestamp = start_time + timedelta(minutes=i)

    # normal location
    city = user_home_city[user]

    device = f'D{random.randint(1,800)}'
    payment_method = random.choice(methods)

    is_fraud = 0

    # inject fraud patterns
    if random.random() < fraud_rate:
        is_fraud = 1

        # pattern 1: large amount spike
        amount *= random.randint(5,15)

        # pattern 2: location anomaly
        city = random.choice([c for c in cities if c != user_home_city[user]])

        # pattern 3: shared fraud device
        device = f'D{random.randint(1,50)}'

    data.append([
        i,user,merchant,amount,timestamp,
        city,payment_method,device,is_fraud
    ])

df = pd.DataFrame(data,columns=[
    'transaction_id','user_id','merchant_id','amount',
    'timestamp','location','payment_method','device_id','is_fraud'
])

df.to_csv("data/transactions.csv",index=False)

print("✅ Data generated: data/transactions.csv")