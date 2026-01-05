import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

os.makedirs("models", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

data = pd.DataFrame([[60,6,1234,80,2]], columns=["frame.len","ip.proto","tcp.srcport","tcp.dstport","tcp.flags"])
data["label"] = 0

X = data.drop("label", axis=1)
y = data["label"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

joblib.dump(scaler, "models/scaler.pkl")
pd.DataFrame(X_scaled).to_csv("data/processed/X.csv", index=False)
y.to_csv("data/processed/y.csv", index=False)
