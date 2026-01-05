import joblib

vectorizer, model = joblib.load("models/phishing_model.pkl")

def analyze_content(text):
    vec = vectorizer.transform([text])
    label = model.predict(vec)[0]
    confidence = model.predict_proba(vec)[0].max()
    return label, confidence