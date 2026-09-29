# Playwright Python BDD Automation Framework

A UI and API automation framework built using **Python, Playwright, Pytest, and Pytest-BDD**.

The project follows the **Page Object Model (POM)** and uses BDD feature files to organize test scenarios. It also includes API testing for creating and managing test orders.

## Tech Stack

* Python
* Playwright
* Pytest
* Pytest-BDD
* Selenium-style Page Object Model
* REST API testing
* JSON test data
* HTML test reports
* Git & GitHub

## Project Structure

```text
playwright/
│
├── features/
│   └── ordersTransaction.feature
│
├── pageObjects/
│   ├── cart.py
│   ├── dashboard.py
│   ├── login.py
│   ├── orderConfirmation.py
│   ├── orderHistory.py
│   └── paymentDetails.py
│
├── steps/
│   └── test_orders_transaction.py
│
├── utils/
│   └── apiBase.py
│
├── data/
│   └── credentials.json
│
├── conftest.py
├── pytest.ini
└── test_*.py
```

## What is Covered

### UI Testing

* User login
* Product selection
* Adding multiple products to the cart
* Verifying products in the cart
* Removing products from the cart
* Checkout process
* Payment details
* Order confirmation
* Order history validation

### API Testing

* User authentication
* Creating orders through API
* Retrieving order information
* Deleting orders
* Validating API responses

### BDD

Test scenarios are written using **Gherkin syntax** and implemented using Pytest-BDD step definitions.

Example:

```gherkin
Scenario: Add multiple products to the cart
    Given user is logged in
    When user adds these products to cart
    Then all the products should be displayed in the cart
```

## Page Object Model

The framework separates page-specific actions from test steps.

For example:

```text
Login
Dashboard
Cart
PaymentDetails
OrderConfirmation
OrderHistory
```

This makes the test code easier to maintain when the application's UI changes.

## Running the Tests

Install the required Python packages:

```bash
pip install pytest
pip install pytest-bdd
pip install playwright
```

Install Playwright browsers:

```bash
playwright install
```

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest steps/test_orders_transaction.py
```

Run tests using a marker:

```bash
pytest -m smoke
```

## Test Reports

The project can generate an HTML test report using `pytest-html`.

Example:

```bash
pytest --html=report.html
```

## Framework Features

* Page Object Model
* BDD with Gherkin
* UI automation with Playwright
* API automation
* Reusable pytest fixtures
* Parameterized test data
* Browser configuration
* HTML test reporting
* Git/GitHub version control

## Purpose

This project was created to practice and demonstrate practical **QA automation skills**, including UI automation, API testing, BDD, framework design, reusable test components, and test reporting.
