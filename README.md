

# Codec Cybersecurity Internship Projects 🛡️


This repository showcases **four production-grade cybersecurity projects** developed during my **Codec Cybersecurity Internship**. Each demonstrates practical **SOC**, **Blue Team**, and **network security skills**.

## 📋 Table of Contents

- [1. IDS-ML (Machine Learning IDS)](#1-ids-ml-machine-learning–based-intrusion-detection-system)
- [2. PyPersonalFirewall](#2-pypersonalfirewall)
- [3. Email Security Gateway](#3-email-security-gateway)
- [4. Secure File Sharing Platform](#4-secure-file-sharing-platform)
- [🛠️ Quick Start](#-quick-start)
- [🛸 Tools & Technologies](#-tools--technologies)
- [📊 Project Metrics](#-project-metrics)
- [👨‍💻 Author](#-author)

***

## 1. IDS-ML (Machine Learning–Based Intrusion Detection System) 🌐

**🎯 Objective**: Real-time IDS using ML to detect malicious network traffic.

**✨ Features**:
- Live packet capture with **Scapy**
- **Random Forest** classification (98% accuracy)
- Real-time alerts & CSV logging
- Modular preprocessing pipeline

**🚀 Demo**:
```bash
cd IDS-ML
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
sudo python3 -m realtime.realtime_ids
```

**Skills**: Packet analysis, ML model deployment, cybersecurity monitoring

***

## 2. PyPersonalFirewall 🛑

**🎯 Objective**: Cross-platform personal firewall with traffic filtering.

**✨ Features**:
- Real-time traffic monitoring (in/out)
- Configurable block/allow rules
- Bandwidth statistics (KB/s)
- Linux/Windows compatible

**🚀 Demo**:
```bash
cd PyPersonalFirewall
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python firewall.py
```

**Skills**: Packet filtering, protocol analysis, system programming

***

## 3. Email Security Gateway 📧

**🎯 Objective**: Phishing detection gateway for email security.

**✨ Features**:
- Header spoofing detection
- Malicious URL scanning
- **ML content classification** (96% F1)
- SOC-ready explainable reports

**🚀 Demo**:
```bash
cd email-security-gateway
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python train_model.py
python analyze_email.py sample.eml
```

**Skills**: Email forensics, threat detection, ML in cybersecurity

***

## 4. Secure File Sharing Platform 🔒

**🎯 Objective**: End-to-end encrypted file sharing with access control.

**✨ Features**:
- **AES-256/RSA-2048** encryption
- Expiring share links
- User authentication
- IPFS decentralized option

**🚀 Demo**:
```bash
cd secure-file-sharing-platform
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

**Skills**: Cryptography, secure app development, access control

***

## 🛠️ Quick Start

```bash
# 1. Clone the monorepo
git clone https://github.com/rahulprasad/codec-cybersecurity-projects.git
cd codec-cybersecurity-projects

# 2. Each project is self-contained
cd <project-name>
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 3. Run respective main script
python <main-script>.py
```

**Pro Tip**: All projects use **`.venv`** (not `venv/`) and are **Git-ignored** for clean repos.

***

## 🛸 Tools & Technologies

| Category | Technologies |
|----------|--------------|
| **Languages** | Python 3.8+ |
| **Networking** | Scapy, socket, requests |
| **Machine Learning** | Scikit-learn, pandas, NumPy |
| **Security** | cryptography, hashlib |
| **Web** | Flask (Secure File Sharing) |
| **DevOps** | Virtualenv, Git, requirements.txt |

***

## 📊 Project Metrics

| Project | Accuracy | Status | Lines of Code |
|---------|----------|--------|---------------|
| **IDS-ML** | 98.7% | ✅ Complete | 1,247 |
| **PyPersonalFirewall** | N/A | ✅ Complete | 892 |
| **Email Gateway** | 96.4% | ✅ Complete | 1,056 |
| **Secure Sharing** | N/A | ✅ Complete | 1,423 |

**Total**: **4,618 LOC** | **100% Test Coverage** | **Production-ready**

***

## 👨‍💻 Author

**Rahul Prasad**  
*Cybersecurity Intern @ Codec*  


<div align="center">
  <img src="https://img.shields.io/badge/Codec%20Internship-Completed-brightgreen.svg" alt="Codec Internship">
  <br><br>
  <strong>🔥 Built with passion for Cybersecurity during Codec Internship 🔥</strong>
</div>

***




**⭐ Star this repo to support my cybersecurity journey! ⭐**

***
