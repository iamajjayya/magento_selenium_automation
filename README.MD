# Magento Selenium Automation using POM

This project is focused on automating an e-commerce website built on Magento using **Selenium WebDriver** in Python. I’ve used the **Page Object Model (POM)** design pattern to make the automation framework clean, reusable, and easy to maintain.

---

## Project Overview

The goal of this project is to automate some common user flows like:

- Logging in to the website
- Searching for products
- Filtering and sorting results
- Adding items to the cart

All the test cases are written using **PyTest**, and the framework is structured to support future enhancements easily.

---

## What is Page Object Model (POM)?

POM is a design pattern that helps separate the page structure (locators and actions) from the test scripts. It helps in:

- Keeping the code clean and organized
- Reusing methods across different test cases
- Making the framework easy to scale and maintain

Each page is represented by a separate Python class, which contains all the elements (locators) and actions (methods) related to that page.

---

## Folder Structure

Here's a breakdown of how I’ve organized the project:

magento_automation/
│
├── config/
│ └── config.py # Stores base URL, login credentials, and browser info
│
├── drivers/
│ └── chromedriver.exe # WebDriver executable for running tests
│
├── pages/
│ ├── base_page.py # Common reusable methods like click(), send_keys(), etc.
│ ├── login_page.py # Handles login actions
│ ├── home_page.py # Actions after login (welcome message, logout, etc.)
│ └── product_page.py # Product search, filters, add to cart, etc.
│
├── tests/
│ ├── test_login.py # Verifies login functionality
│ └── test_cart.py # Verifies that products can be added to cart
│
└── README.md # Project documentation


---

## Tools & Technologies Used

- Python
- Selenium WebDriver
- PyTest
- Git & GitHub
- (Optional: Jenkins, Docker for CI/CD)

---

## How to Run the Project

1. Clone this repo to your local system
2. Install the dependencies using pip (I'll add a `requirements.txt` file)
3. Add your own `chromedriver.exe` file in the drivers folder
4. Update `config.py` with your Magento test credentials and base URL
5. Run the tests using:


---

## Final Note

This project is still a work in progress and I plan to add more test cases like checkout, user registration, etc. I’ve tried to keep it simple and readable so anyone can understand and contribute easily.

If you’ve any suggestions or feedback, feel free to reach out!

---

**Author:**
Ajjayya G V
Automation Tester | Python | Selenium | PyTest | POM
