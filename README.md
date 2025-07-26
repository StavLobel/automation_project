# 🚀 Professional Selenium Test Automation Framework

**Enterprise-grade UI automation testing for web applications using Python, Selenium, and Pytest**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)](https://selenium-python.readthedocs.io/)
[![Pytest](https://img.shields.io/badge/Pytest-Latest-orange.svg)](https://docs.pytest.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-blue.svg)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-black.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/Pre--commit-Enabled-green.svg)](https://pre-commit.com/)

---

## 🎯 About This Project

This repository showcases a **production-ready test automation framework** designed for modern web application testing. Built with industry best practices and enterprise standards, it demonstrates professional software testing methodologies that are commonly used in high-performing development teams.

### 🏆 **What Makes This Project Professional**

- **Industry-Standard Architecture**: Implements the Page Object Model (POM) design pattern for maintainable and scalable test code
- **Comprehensive Test Coverage**: Demonstrates thorough testing strategies including positive flows, negative scenarios, and edge cases
- **Modern Development Practices**: Integrates CI/CD pipelines, code quality tools, and automated reporting
- **Production-Ready Features**: Includes error handling, logging, environment management, and performance optimization
- **Professional Documentation**: Comprehensive setup guides, architecture diagrams, and best practice documentation

### 🎯 **Perfect For**

- **QA Engineers** looking to demonstrate advanced automation skills
- **Test Automation Specialists** showcasing enterprise-level frameworks
- **Software Engineers** learning professional testing methodologies
- **Interview Preparation** for automation-focused roles
- **Team Lead Positions** requiring framework design experience

### 🚀 **Key Demonstrations**

- **Test Framework Design**: Modular, maintainable, and scalable architecture
- **CI/CD Integration**: Automated testing with GitHub Actions and comprehensive reporting
- **Code Quality**: Black formatting, pre-commit hooks, and linting standards
- **Security Best Practices**: Environment variable management and credential handling
- **Performance Optimization**: Parallel execution, smart waits, and resource management

---

## 🎯 Project Overview

A comprehensive test automation framework demonstrating industry best practices for web application testing. Built with modern Python tools and designed for scalability, maintainability, and reliability in professional testing environments.

### ✨ Key Features

- **Page Object Model (POM)** - Maintainable and reusable test structure
- **Comprehensive Test Coverage** - Login flows, shopping cart functionality, edge cases
- **CI/CD Integration** - Automated testing with GitHub Actions
- **Professional Reporting** - HTML and JUnit XML reports with detailed logs
- **Code Quality** - Black formatting, pre-commit hooks, and linting
- **Environment Management** - Secure credential handling with .env files

---

## 🛠️ Technology Stack

- **Testing Framework**: Pytest
- **Web Automation**: Selenium WebDriver
- **Language**: Python 3.x
- **CI/CD**: GitHub Actions
- **Code Quality**: Black, pre-commit hooks
- **Reporting**: pytest-html, JUnit XML
- **Test Site**: SauceDemo (industry-standard demo application)

---

## 📁 Architecture

```
src/
  └── pages/                    # Page Object Model
      ├── base_page.py          # Base class with common functionality
      ├── login_page.py         # Login page interactions
      ├── products_page.py      # Product catalog interactions
      └── cart_page.py          # Shopping cart interactions

tests/
  ├── conftest.py              # Global test configuration and fixtures
  ├── 01-login/               # Login test suite
  │   └── test_login.py       # Authentication tests
  └── 02-cart/                # Shopping cart test suite
      ├── conftest.py         # Cart-specific fixtures
      ├── test_cart_basic.py  # Core cart functionality
      ├── test_cart_edge.py   # Edge case scenarios
      └── test_cart_persistence.py # State persistence tests

.github/workflows/ci.yml      # Continuous Integration pipeline
requirements.txt              # Python dependencies
.pre-commit-config.yaml       # Code quality automation
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/StavLobel/automation_project.git
   cd automation_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   # Create .env file with test credentials
   echo "SAUCE_USERNAME=standard_user" > .env
   echo "SAUCE_PASSWORD=secret_sauce" >> .env
   ```

4. **Run tests**
   ```bash
   # Execute all tests
   pytest tests/
   
   # Run with detailed reporting
   pytest tests/ --html=report.html --self-contained-html
   ```

---

## 🧪 Test Coverage

### Authentication Testing
- ✅ Valid user login flows
- ✅ Invalid credential handling
- ✅ Account lockout scenarios
- ✅ Special character input validation
- ✅ Empty field validation

### Shopping Cart Functionality
- ✅ Add/remove single and multiple items
- ✅ Cart badge count accuracy
- ✅ Price calculation verification
- ✅ Item persistence across sessions
- ✅ Edge case handling (rapid actions, double operations)

### Advanced Scenarios
- ✅ Cross-browser compatibility
- ✅ Responsive design testing
- ✅ Performance under load
- ✅ Error handling and recovery
- ✅ Data persistence validation

---

## 🔧 Development Workflow

### Code Quality Standards
```bash
# Format code with Black
black .

# Install pre-commit hooks
pre-commit install

# Run all quality checks
pre-commit run --all-files
```

### Test Execution Options
```bash
# Run specific test suite
pytest tests/01-login/

# Run with verbose output
pytest -v tests/

# Generate comprehensive reports
pytest tests/ --junitxml=test-results.xml --html=test-report.html --self-contained-html
```

---

## 📊 CI/CD Pipeline

### GitHub Actions Workflow
- **Trigger**: Push to main branch and pull requests
- **Environment**: Ubuntu latest with Python 3.x
- **Steps**:
  1. Code checkout and dependency installation
  2. Code formatting validation (Black)
  3. Pre-commit hook execution
  4. Test execution with reporting
  5. Artifact generation and storage

### Generated Artifacts
- 📄 **JUnit XML Report** - For CI/CD integration
- 📊 **HTML Report** - Human-readable test results
- 📋 **Test Logs** - Detailed execution information

---

## 🏗️ Best Practices Implemented

### Design Patterns
- **Page Object Model** - Separation of test logic from page interactions
- **Factory Pattern** - Dynamic test data generation
- **Fixture Pattern** - Reusable test setup and teardown

### Code Quality
- **Type Hints** - Enhanced code readability and IDE support
- **Docstrings** - Comprehensive documentation
- **Error Handling** - Robust exception management
- **Logging** - Detailed execution tracking

### Test Management
- **Modular Structure** - Organized by functionality
- **Data-Driven Testing** - Parameterized test scenarios
- **Parallel Execution** - Optimized test runtime
- **Environment Isolation** - Secure credential management

---

## 📈 Performance & Scalability

### Optimization Features
- **Parallel Test Execution** - Reduced total execution time
- **Smart Waits** - Optimized element interaction timing
- **Resource Management** - Efficient browser session handling
- **Caching Strategies** - Improved test data access

### Monitoring & Reporting
- **Real-time Logging** - Live test execution feedback
- **Performance Metrics** - Test execution time tracking
- **Failure Analysis** - Detailed error investigation tools
- **Trend Analysis** - Historical test result tracking

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository** and create a feature branch
2. **Install development dependencies** and pre-commit hooks
3. **Write tests** for new functionality
4. **Follow code style** guidelines (Black formatting)
5. **Update documentation** as needed
6. **Submit a pull request** with clear description

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Set up pre-commit hooks
pre-commit install

# Run quality checks
pre-commit run --all-files
```

---

## 📚 Resources & References

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Framework](https://docs.pytest.org/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [SauceDemo Test Site](https://www.saucedemo.com/)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> **Built for professional test automation excellence** 🎯

*Demonstrating industry best practices in web application testing automation*