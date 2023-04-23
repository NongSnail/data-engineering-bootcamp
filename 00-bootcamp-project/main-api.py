import requests
import pandas as pd

API_URL = "http://34.87.139.82:8000/"
DATA = ["events","addresses","order-items","orders","products","promos","users"]

for x in DATA:
    response = requests.get(f"{API_URL}/{x}")
    data = response.json()
    df = pd.DataFrame.from_records(data)
    filepath = f"./data/{x}.csv"
    df.to_csv(filepath)  
    # print(df)