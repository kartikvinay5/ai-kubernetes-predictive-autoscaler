import pickle
import time
import numpy as np
import subprocess

# load trained model
with open("load_model.pkl", "rb") as f:
    model = pickle.load(f)

print("AI Autoscaler Started...")

while True:

    current_time = np.array([[time.time()]])
    prediction = model.predict(current_time)

    predicted_load = prediction[0]

    print("Predicted Load:", predicted_load)

    if predicted_load > 0.8:
        print("High load detected! Scaling pods...")

        subprocess.run([
    "kubectl",
    "scale",
    "deployment/hello-minikube",
    "--replicas=5",
    "-n",
    "default"
])

    time.sleep(30)