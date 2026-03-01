<div align="center">

# 🔍 api-ulp Search Tool

**A simple Python script to search leaked data using the api-ulp package**

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![PyPI](https://img.shields.io/badge/pip_install-api--ulp-orange?style=for-the-badge&logo=pypi)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 📖 About

This project is a simple ready-to-use script that wraps the **api-ulp** pip package.  
Enter your API key, a query (domain, email, username…), and a limit — results are printed and **automatically saved** to a `.txt` file.

The core package is published separately on PyPI:

```
pip install api-ulp
```

---

## 🚀 Quick Setup

**1. Clone this repo**
```bash
git clone https://github.com/rikixz/api-ulp.git
cd api-ulp
```

**2. Install the dependency**
```bash
pip install -r requirements.txt
```

**3. Edit `main.py` and fill in your details**
```python
API_KEY = "YOUR_API_KEY"   # Your api-ulp API key
QUERY   = "example.com"    # Domain, email, username, etc.
LIMIT   = 100              # Max results to return
```

**4. Run it**
```bash
python main.py
```

---

## 💾 Output

On every successful search, results are saved to:
```
results/<query>_<timestamp>.txt
```

Example file content:
```
ULP API Search Results
========================================
Query     : example.com
Limit     : 100
Timestamp : 2025-01-01 12:00:00
========================================

{
  "status": "success",
  "data": { ... }
}
```

---

## 📋 Requirements

- Python `3.7+`
- `api-ulp` (auto-installed via `requirements.txt`)

---

## 📂 Project Structure

```
api-ulp/
├── main.py            # Main script — edit this to run searches
├── requirements.txt   # pip install api-ulp
├── LICENSE            # MIT
└── README.md
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Developer

<div align="center">

### Kris

🎂 **Age:** 17 years old  
💻 **Role:** Solo Developer  
🌏 **Interests:** Python · APIs · Automation · Building useful tools  

> *"17 years old and already shipping real tools to PyPI. Just getting started."*

📦 PyPI → [pypi.org/user/rikixz](https://pypi.org/user/rikixz)  
🐙 GitHub → [github.com/rikixz](https://github.com/rikixz)

</div>

---

<div align="center">

Made with ❤️ by **Kris** · 2025

</div>