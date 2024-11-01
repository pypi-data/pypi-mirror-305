# Recaptcha Solver

A Python package to automatically solve Google reCAPTCHA using Selenium.

## Features

- Automatically detects and solves Google reCAPTCHA challenges.
- Uses Selenium for browser automation.
- Compatible with Windows, macOS, and Linux.

## Requirements

- Python 3.6 or higher
- Chrome WebDriver (ensure it matches your Chrome browser version)
- FFmpeg (auto-downloaded if not available)

## Installation

```bash
pip install recaptcha_solver_google
```

## Code Usage

```bash
from selenium import webdriver
from recaptcha_solver.solver import solve_captcha_for_google_recaptcha

# Initialize the WebDriver and navigate to the reCAPTCHA page
driver = webdriver.Chrome()
driver.get("DESIRED_URL_WHERE_GOOGLE_CAPTCHA_APPEARED")

# Solve the CAPTCHA
solve_captcha_for_google_recaptcha(driver)

# Close the WebDriver
driver.quit()
```
