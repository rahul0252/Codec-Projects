# Secure File Sharing Platform

A **Secure File Sharing Platform** implementing **end-to-end encryption (E2EE)**, **expiring share links**, and **strict access control**. The system is designed using modern cryptographic practices and a zero-knowledge server model, making it suitable for cybersecurity portfolios, academic projects, and secure systems demonstrations.

---

## 🚀 Project Overview

This project allows users to securely upload and share files while ensuring:

* The server **never sees plaintext data**
* Files are protected using strong cryptography
* Shared links can expire or be revoked
* Unauthorized access is prevented

The platform follows a **hybrid encryption model** combining symmetric and asymmetric cryptography for both performance and security.

---

## 🔐 Key Security Features

* **End-to-End Encryption (E2EE)**
* **AES-256-GCM** for file encryption
* **RSA-2048** for secure key exchange
* **SHA-256** for integrity verification
* **Expiring & revocable share links**
* **Zero-knowledge server architecture**
* Protection against replay attacks and brute-force attempts

---

## 🧱 Technology Stack

### Backend

* Python 3
* Django
* Django REST Framework
* Cryptography (Python library)

### Security & Cryptography

* AES-256-GCM
* RSA-2048
* SHA-256

### Database

* SQLite (development)
* PostgreSQL (recommended for production)

### Optional

* IPFS (for decentralized encrypted storage)

---

## 🏗️ Project Architecture

```
Client (Browser / CLI)
│
│  Client-side Encryption (AES)
│  RSA Public Key Encryption
│
▼
Django REST API
│
├── Authentication & Authorization
├── File Metadata Management
├── Access Control & Expiry Validation
│
▼
Encrypted Storage (Local / Cloud / IPFS)
```

> **Important:** All encryption happens on the client side. The backend only stores encrypted data and metadata.

---

## 📁 Project Structure

```
secure-file-sharing-platform/
├── backend/
│   ├── api/
│   ├── crypto/
│   │   └── crypto_utils.py
│   ├── models/
│   │   └── models.py
│   ├── views/
│   │   └── file_views.py
│   └── storage/
├── docs/
│   ├── architecture.md
│   └── threat_model.md
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup (Using `.venv`)

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/secure-file-sharing-platform.git
cd secure-file-sharing-platform
```

---

### 2️⃣ Create a Virtual Environment (`.venv`)

```bash
python3 -m venv .venv
```

Activate the virtual environment:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\\Scripts\\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Django Setup

Initialize the Django project (if not already initialized):

```bash
django-admin startproject backend
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser (optional):

```bash
python manage.py createsuperuser
```

---

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

The server will be available at:

```
http://127.0.0.1:8000/
```

---

## 🔑 Cryptographic Workflow

1. Client generates a random AES-256 session key
2. File is encrypted locally using AES-GCM
3. AES key is encrypted using recipient's RSA public key
4. Server stores:

   * Encrypted file
   * Encrypted AES key
   * Metadata only

✔️ The server never has access to plaintext files or keys

---

## ⏳ Expiring & Secure Share Links

* Cryptographically secure random tokens
* Optional password protection
* Maximum download limits
* Automatic expiry timestamps
* Manual revocation support

---

## 🛡️ Threat Model & Mitigations

| Threat              | Mitigation                         |
| ------------------- | ---------------------------------- |
| Server breach       | End-to-End Encryption              |
| Brute-force links   | Long random tokens + rate limiting |
| Replay attacks      | Nonce + expiry timestamps          |
| Unauthorized access | Access control & validation        |
| File tampering      | SHA-256 integrity checks           |

Detailed analysis available in `docs/threat_model.md`.

---

## 📈 Future Enhancements

* JWT-based authentication
* Role-based access control (RBAC)
* IPFS-based encrypted storage
* React frontend
* Audit logging & monitoring
* Docker & Docker Compose support
* HTTPS + HSTS enforcement

---

## 🎯 Use Cases

* Cybersecurity portfolio project
* Secure cloud storage prototype
* Academic / IEEE project
* Internship & placement evaluations
* Secure data sharing demonstrations

---

## 📜 License

This project is intended for **educational and research purposes**. You are free to extend and modify it for personal or academic use.

---

## 👤 Author

**Rahul Prasad**
Computer Science & Engineering Undergraduate
Cybersecurity | Secure Systems | Applied Cryptography

---

