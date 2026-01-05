# Email Security Gateway with Phishing Detection

A Python-based email security gateway that detects phishing emails using:
- Email header analysis
- URL inspection
- Machine Learning (TF-IDF + Logistic Regression)

## Features
- From / Reply-To mismatch detection
- Suspicious URL heuristics
- ML-based phishing classification
- CLI-based analysis

## How to Run
```bash
pip install -r requirements.txt
python train_model.py
python analyze_email.py
```

## Disclaimer
Educational and defensive use only.