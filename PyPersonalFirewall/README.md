# PyPersonalFirewall 🔥

A **cross-platform personal firewall and network traffic monitoring application** built with **Python**. The project provides a **GUI-based dashboard** to visualize real-time inbound and outbound network traffic and demonstrates how firewall logic can be integrated on Linux and Windows systems.

This project is designed for:

* Cybersecurity students
* Internship / academic submissions
* Portfolio demonstration of network security concepts

---

## ✨ Features

* 📊 **Real-time traffic visualization** (Incoming / Outgoing KB/s)
* 🖥️ **Modern GUI dashboard** using Tkinter
* 📈 Live traffic graph (Matplotlib)
* 🔐 Firewall integration support:

  * Linux → `iptables`
  * Windows → Windows Firewall (`netsh`)
* 🧪 Monitoring-only mode on macOS (safe & non-intrusive)
* 🧩 Modular, clean, GitHub-ready project structure

---

## 🧠 What Traffic Is Analyzed?

Currently, PyPersonalFirewall analyzes:

> **Aggregate system-wide network traffic at the network interface level**

This includes:

* All inbound and outbound traffic across all applications
* All protocols (TCP, UDP, ICMP, etc.)
* Background OS and user-generated traffic

Traffic speed is calculated in **real-time (KB/s)** using OS kernel counters via `psutil`.

> ⚠️ Note: This version does **not** perform packet inspection, port-level filtering, or process-level attribution. It focuses on monitoring and visualization.

---

## 🗂️ Project Structure

```
PyPersonalFirewall/
│
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── core/
│   ├── firewall_linux.py      # iptables integration (Linux)
│   ├── firewall_windows.py    # Windows Firewall integration
│   └── traffic_monitor.py     # Real-time traffic rate calculation
│
├── gui/
│   ├── dashboard.py           # Main GUI layout
│   └── traffic_dashboard.py   # Live traffic graph
│
└── utils/
    └── platform_check.py      # OS detection logic
```

---

## 🧰 Requirements

* Python **3.9+**
* Operating System:

  * ✅ Linux (Full firewall support)
  * ✅ Windows (Firewall support)
  * ⚠️ macOS (Monitoring-only mode)

---

## 🐍 Python Virtual Environment (.venv) Setup (Recommended)

It is **strongly recommended** to use a virtual environment to avoid dependency conflicts.

### 1️⃣ Create a virtual environment

```bash
python3 -m venv .venv
```

### 2️⃣ Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Application

### macOS

> Runs in **monitoring-only mode** (no firewall enforcement)

```bash
python3 main.py
```

### Linux

> Requires root privileges for firewall control

```bash
sudo python3 main.py
```

### Windows

> Run terminal as **Administrator**

```powershell
python main.py
```

---

## 🧪 How to Test Live Traffic

Generate traffic while the app is running:

```bash
ping google.com
curl https://example.com
```

You should see:

* Incoming KB/s changing
* Outgoing KB/s changing
* Graph updating every second

---

## 🔒 Firewall Capabilities

| Platform | Capability                  |
| -------- | --------------------------- |
| Linux    | iptables-based rule control |
| Windows  | Windows Firewall (netsh)    |
| macOS    | Monitoring only             |

Firewall logic is modular and can be extended to support:

* Custom rules
* Port blocking
* IP blacklisting

---

## 🚀 Future Enhancements

* Per-process network traffic visualization
* Port-wise traffic analysis
* IDS / anomaly detection using ML
* Threat intelligence integration
* Alert system with thresholds
* Dark-mode GUI

---

## 🎓 Academic & Portfolio Value

This project demonstrates:

* Network traffic analysis
* OS-level firewall concepts
* Secure Python application design
* Real-time GUI data visualization
* Cross-platform system programming

Ideal for:

* Cybersecurity internships
* SOC / Blue Team portfolios
* Academic evaluations

---

## 📜 Disclaimer

This project is intended for **educational purposes only**.
Use firewall features responsibly and only on systems you own or are authorized to test.

---

## 👤 Author

**Rahul Prasad**
Computer Science & Engineering Undergraduate
Cybersecurity & Network Security Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or extend it.

---

**Happy Securing!** 🔐
