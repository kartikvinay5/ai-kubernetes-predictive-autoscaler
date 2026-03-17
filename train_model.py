import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("metrics_dataset.csv")

# Feature and target
X = data[['timestamp']]
y = data['service_status']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("load_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")