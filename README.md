# 🚀 SauceDemo Automation Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Testing-blueviolet?logo=pytest)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/StavLobel/automation_project/ci.yml?label=CI&logo=github)

---

## 📝 Overview
Automated UI testing for [SauceDemo](https://www.saucedemo.com) using **Python**, **Selenium**, and **Pytest**. This project demonstrates:
- Professional test structure (Page Object Model, fixtures, modularity)
- Robust test coverage (login, cart, edge cases)
- CI/CD with GitHub Actions
- Code quality with Black & pre-commit hooks

---

## 📁 Project Structure

```text
src/
  └── pages/
      ├── base_page.py         # Base class for all page objects
      ├── login_page.py        # Login page object
      ├── products_page.py     # Products/inventory page object
      └── cart_page.py         # Cart page object

tests/
  ├── conftest.py             # Global fixtures
  ├── 01-login/
  │   └── test_login.py       # Login test suite
  └── 02-cart/
      ├── conftest.py         # Cart-specific fixtures
      ├── test_cart_basic.py  # Basic cart tests
      ├── test_cart_edge.py   # Cart edge case tests
      └── test_cart_persistence.py # Cart persistence tests

.github/workflows/ci.yml      # GitHub Actions workflow
requirements.txt              # Python dependencies
.pre-commit-config.yaml       # Pre-commit hooks config
.env (not committed)          # Environment variables
README.md                     # Project documentation
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/StavLobel/automation_project.git
   cd automation_project
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pytest-html
   ```
3. **Set up environment variables**
   - Create a `.env` file in the root directory:
     ```env
     SAUCE_USERNAME=standard_user
     SAUCE_PASSWORD=secret_sauce
     ```

---

## 🤖 Running Tests

- **All tests:**
  ```bash
  pytest tests/
  ```
- **Specific suite:**
  ```bash
  pytest tests/01-login/
  pytest tests/02-cart/test_cart_edge.py
  ```
- **Generate HTML & JUnit reports:**
  ```bash
  pytest tests/ --junitxml=pytest-report.xml --html=pytest-report.html --self-contained-html --capture=tee-sys --log-cli-level=INFO
  ```

---

## 🖥️ CI/CD & Artifacts

- **GitHub Actions** runs all tests and code formatting on every push/PR.
- Artifacts:
  - 📝 `pytest-report.xml` (JUnit XML)
  - 📊 `pytest-report.html` (HTML, with logs)
- Download artifacts from the Actions tab after each run.

---

## 🧪 Features & Test Coverage

### 🔑 Login
- Valid login
- Invalid login (wrong credentials, empty fields, locked out user, special characters)

### 🛒 Cart
- Add/remove single/multiple items
- Cart badge/count updates
- Edge cases: add/remove in random order, double remove, badge visibility, rapid actions
- Persistence: after refresh, navigation, logout/login, clearing cookies

---

## 👩‍💻 Contributing

1. Fork the repo & create a branch
2. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```
3. Run Black before committing:
   ```bash
   black .
   ```
4. Open a PR with a clear description

---

## 📚 References
- [SauceDemo](https://www.saucedemo.com)
- [Selenium Docs](https://www.selenium.dev/documentation/)
- [Pytest Docs](https://docs.pytest.org/)
- [pytest-html](https://pypi.org/project/pytest-html/)

---

## 💡 Tips
- Use the HTML report for a visual summary and logs
- All credentials are managed via `.env` for security
- Structure your own tests in new files/folders for clarity

---

> Made with ❤️ for professional automation and interview success!
