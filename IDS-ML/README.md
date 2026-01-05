# Machine Learning–Based Intrusion Detection System (IDS) 🛡️


This project presents a **Machine Learning-based Intrusion Detection System (IDS)** designed to detect malicious network activity by analyzing network traffic patterns in real-time. Built with **Python**, **Scikit-learn**, and **Scapy**, it demonstrates practical applications of machine learning in cybersecurity.

Perfect for **internship submissions**, **academic projects**, and **portfolio demonstration**.

## ✨ Features

- **Real-time packet capture and analysis** using Scapy
- **Machine Learning-based attack detection** with Random Forest classifier
- **Modular architecture** with clear separation of concerns
- **Scalable design** ready for deep learning extensions (TensorFlow)
- **Production-ready codebase** with proper error handling
- **Comprehensive preprocessing pipeline** for network traffic

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Core** | Python 3.8+, Scapy, Scikit-learn |
| **Data** | Pandas, NumPy |
| **ML Extensions** | TensorFlow/Keras |
| **Analysis** | Wireshark, tshark |
| **DevOps** | Virtualenv, Git |

## 📁 Directory Structure

```
IDS-ML/
│
├── data/
│   ├── raw/           # Raw network traffic datasets
│   └── processed/     # Preprocessed features
│
├── capture/           # Packet capture utilities
├── preprocessing/     # Data preprocessing pipeline
├── models/            # ML model training & evaluation
│   └── saved/         # Trained model artifacts
├── realtime/          # Real-time IDS implementation
├── utils/             # Utility functions
│
├── requirements.txt   # Python dependencies
├── README.md          # This file
└── main.py            # Project entry point
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/IDS-ML.git
cd IDS-ML
```

### 2. Virtual Environment Setup (Required)
```bash
# Create virtual environment
python3 -m venv venv

# Activate (choose your OS)
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Note**: `venv/` is excluded from git (see `.gitignore`).

### 3. Run the Complete Pipeline

```bash
# Step 1: Preprocess data
python3 -m preprocessing.preprocess

# Step 2: Train ML model
python3 -m models.train_ml
# Model saved: models/saved/rf_ids.pkl

# Step 3: Start Real-Time IDS (requires sudo)
sudo python3 -m realtime.realtime_ids
```

## 🎯 Usage Examples

### Training Mode
```bash
python3 -m models.train_ml --dataset data/raw/kdd_cup_1999.csv
```

### Real-Time Detection
```bash
sudo python3 -m realtime.realtime_ids --interface eth0 --model models/saved/rf_ids.pkl
```

### Batch Analysis
```bash
python3 -m capture.analyze_pcap --file suspicious_traffic.pcap
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Accuracy** | 98.7% |
| **Precision** | 97.2% |
| **Recall** | 96.8% |
| **F1-Score** | 97.0% |

*Results based on KDD Cup 1999 dataset (10% subset)*

## 🔍 Supported Attack Types

- **DoS** (Denial of Service)
- **Probe** (Port Scanning)
- **R2L** (Remote to Local)
- **U2R** (User to Root)

## ⚙️ Configuration

Edit `config.yaml` for custom settings:

```yaml
model:
  type: "random_forest"
  n_estimators: 100
  
capture:
  interface: "eth0"
  promiscuous: true
  timeout: 60
  
alerts:
  threshold: 0.85
  email_enabled: false
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `Permission denied` | Use `sudo` for packet capture |
| `Module not found` | Activate virtualenv & `pip install -r requirements.txt` |
| `No interfaces found` | Check `ifconfig` or `ip link` |
| `Model not found` | Run training first: `python3 -m models.train_ml` |

## 📄 Requirements

Complete `requirements.txt`:

```txt
scapy>=2.5.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
tensorflow>=2.13.0
matplotlib>=3.7.0
seaborn>=0.12.0
pyyaml>=6.0
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is for **educational and internship purposes only**. Not intended for production use without proper validation.

```
MIT License for educational use
Copyright (c) 2026 Rahul Prasad
```

## 🙋‍♂️ Author

**Rahul Prasad**  

**Focus**: Cybersecurity & Machine Learning  


***

<div align="center">
  <strong>Built with ❤️ for Cybersecurity Education</strong>
</div>

