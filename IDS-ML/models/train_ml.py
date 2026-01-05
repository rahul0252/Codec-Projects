import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Ensure model directory exists
os.makedirs("models/saved", exist_ok=True)

# Feature schema (MUST match real-time extractor)
FEATURE_COLUMNS = [
    "frame.len",
    "ip.proto",
    "tcp.srcport",
    "tcp.dstport",
    "tcp.flags"
]

# Load processed data with enforced feature order
X = pd.read_csv("data/processed/X.csv")[FEATURE_COLUMNS]
y = pd.read_csv("data/processed/y.csv").values.ravel()

# Train model
model = RandomForestClassifier(
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)
model.fit(X, y)

# Save model
joblib.dump(model, "models/saved/rf_ids.pkl")

print("Model trained and saved successfully")

