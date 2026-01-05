from scapy.all import sniff
import joblib
from utils.feature_extractor import extract_features


model = joblib.load("models/saved/rf_ids.pkl")

def detect(packet):
    features = extract_features(packet)
    pred = model.predict([features])[0]
    if pred == 1:
        print("[ALERT] Malicious Packet Detected")

sniff(prn=detect, store=False)
