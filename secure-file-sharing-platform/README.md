# Secure File Sharing Platform

## Objective
A secure file sharing platform with end-to-end encryption, expiring links, and access control.

## Tech Stack
- Python
- Django + Django REST Framework
- AES-256-GCM + RSA-2048
- SQLite (dev)

## Features
- Client-side encryption
- Secure upload & download
- Expiring share links
- Access control
- Cryptographic integrity checks

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Security
- Zero-knowledge server design
- AES for file encryption
- RSA for key exchange
- SHA-256 for integrity

## Author
Cybersecurity Project
