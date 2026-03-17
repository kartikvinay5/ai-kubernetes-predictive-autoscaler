import requests
import pandas as pd
import time

PROM_URL = "http://localhost:9090/api/v1/query"

query = "up"

data = []

print("Collecting metrics...")

for i in range(50):

    response = requests.get(PROM_URL, params={"query": query})
    result = response.json()

    value = float(result["data"]["result"][0]["value"][1])

    timestamp = time.time()

    data.append({
        "timestamp": timestamp,
        "service_status": value
    })

    print("Collected:", value)

    time.sleep(5)

df = pd.DataFrame(data)

df.to_csv("metrics_dataset.csv", index=False)

print("Dataset saved!")