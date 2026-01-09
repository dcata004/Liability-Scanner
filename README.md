<div align="center">

# 📜 Liability Scanner
### Automated Vendor Contract Forensics
**Part of the Cata Risk Lab Sovereign Audit Suite**

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/Cata-Risk-Lab/Liability-Scanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)

</div>

---

## 🚨 The Problem
Most AI vendors bury "Right to Train" clauses deep in their Terms of Service. 
For regulated entities (Banks, Healthcare), inadvertently granting a vendor a **"perpetual, worldwide, royalty-free license"** to use uploaded data for model training is a massive compliance violation (GDPR / nFADP).

## 🛡️ The Solution
**Liability Scanner** is a forensic crawler that:
1.  Fetches the raw text of a Vendor's Legal/Terms page.
2.  Scans for specific adversarial legal patterns.
3.  Flags high-risk clauses that threaten Data Sovereignty.

### Detected Risk Patterns
* *"Perpetual, irrevocable license"*
* *"Right to improve our services"* (often code for training)
* *"Royalty-free, worldwide"*
* *"Train our models"*

---

## 🚀 Usage

### Option 1: Live Cloud Demo (Recommended)
Run the scanner instantly without installation on our Hugging Face Space:
👉 **[Launch Liability Scanner](https://huggingface.co/spaces/Cata-Risk-Lab/Liability-Scanner)**

### Option 2: Local Installation
```bash
# Clone the repository
git clone [https://github.com/dcata004/Liability-Scanner.git](https://github.com/dcata004/Liability-Scanner.git)

# Install dependencies
pip install gradio requests beautifulsoup4

# Run the auditor
python app.py
