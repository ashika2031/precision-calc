cat > README.md << 'MD'
# 🧮 Precision Calc — Modular Command-Line Calculator

[![Build Status](https://github.com/ashika2031/precision-calc/actions/workflows/python-app.yml/badge.svg)](https://github.com/ashika2031/precision-calc/actions)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

A **modular, professional-grade command-line calculator** built in Python.  
This project demonstrates best practices in clean architecture, testing, and continuous integration (CI/CD) using **GitHub Actions**.

---

## 🚀 Features

- **REPL Interface** — Interactive command-line loop
- **Supported Operations:**
  - ➕ Addition (`add` or `+`)
  - ➖ Subtraction (`subtract` or `-`)
  - ✖️ Multiplication (`multiply` or `*`)
  - ➗ Division (`divide` or `/`)
- **Special Commands**
  - `help` → View command usage
  - `history` → Show recent calculations
  - `exit` / `quit` → Exit the REPL
- **Robust Error Handling**
  - Handles invalid input, missing arguments, and division by zero gracefully
- **Testing**
  - 100% test coverage enforced via `pytest` + `pytest-cov`
- **CI/CD**
  - GitHub Actions pipeline runs all tests on each push
  - Build fails automatically if coverage < 100%

---

## 🧱 Project Structure

precision-calc/
├── app/
│ ├── init.py
│ ├── operation/
│ │ ├── init.py
│ │ └── operations.py
│ ├── calculation/
│ │ ├── init.py
│ │ ├── calculation.py
│ │ ├── factory.py
│ │ └── history.py
│ └── calculator/
│ ├── init.py
│ ├── cli.py
│ └── main.py
├── tests/
│ ├── init.py
│ └── test_calculations.py
├── .github/
│ └── workflows/
│ └── python-app.yml
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ashika2031/precision-calc.git
cd precision-calc
2️⃣ Create and Activate a Virtual Environment
bash
Copy code
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy code
python -m app.calculator
Example:

markdown
Copy code
Calculator — type 'help' for commands. Ctrl+C to exit.
> add 2 3
5.0
> multiply 4 5 6
120.0
> history
1. add(2.0, 3.0) = 5.0
2. multiply(4.0, 5.0, 6.0) = 120.0
> quit
Goodbye!
🧪 Testing and Coverage
Run all tests:

bash
Copy code
pytest
Generate a detailed coverage report:

bash
Copy code
pytest --cov=app --cov-report=term-missing
Expected output:

markdown
Copy code
Name                             Stmts   Miss  Cover
----------------------------------------------------
app/calculator/cli.py               45      0   100%
TOTAL                              103      0   100%
🧰 Continuous Integration (GitHub Actions)
This project uses GitHub Actions for CI/CD automation.

Workflow Highlights
Runs on every push or pull request

Uses Python 3.11

Enforces 100% coverage with coverage report --fail-under=100

File: .github/workflows/python-app.yml

yaml
Copy code
- name: Run tests with coverage
  run: |
    pytest --cov=app --cov-report=term-missing tests/
- name: Enforce 100% coverage
  run: |
    coverage report --fail-under=100
