Project Overview: Magento Selenium Automation using POM

The Goal of this project is to automate on a Magento e-commerce website
(like login,product,search,add to cart,etc) using Selenium webdriver with Page Object Model(POM) Design

POM -> Approach helps organize your test code by separating the page structure(locators and actions) from the test scripts
making code clean, reusable, and easy to maintain

What is Page Object Model(POM)?

Page Object Model is a design pattern that creates an object repository for web UI Elements
It separates:

* Test scripts( what to test)
* Page Classes(How to interact with the page)

Detailed Explanation of File Structure 
--------------------------------------

magento_automation/

config
 -> config.py
 -> Holds configuration data like base URL,login credentials, and browser settings

drivers
  -> chromedriver.exe
  -> Stores the Webdriver executable (like chromedriver.exe or geokodriver for firefox)

This is the Heart of POM:
-> Each page class represents a single web page with:
    -> Locators(how to find elements)
    -> Methods(actions like click_login(), search_product())

  ->base_page.py -> common reusable methods like click(),send_keys(),wait_for_element()
  ->login_page.py -> Handles login screen(input/password, click login)
  ->home_page.py -> Handles hp actions(welcome messages, categories, logout)
  -> Product_page.py -> Deals with product search, add to cart, filter , sort, etc

Tests/
   -> test_login.py - example test case using login_page
   -> test_cart.py  - verifies product addition to cart

