import requests
import pandas as pd

API_URL = "http://34.87.139.82:8000/"
DATA = "events"
DATE = "2021-02-11"

response = requests.get(f"{API_URL}/{DATA}")
data = response.json()
# print(data)
# for each in data:
    # print(each["event_id"], each["event_type"])
    
df = pd.DataFrame.from_records(data)
print(df)