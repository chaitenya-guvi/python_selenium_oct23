from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os

# Specify the browser type
browser_type = 'chrome'  # or 'firefox', 'edge', etc.

# Check if WebDriver Manager has downloaded the driver
driver_path = webdriver.__file__
print(driver_path)
if not os.path.exists(driver_path):
    raise WebDriverException(f"WebDriver Manager failed to locate {browser_type} driver binary.")

# Continue with your test code
driver = webdriver.Firefox()
try:
    # Initialize the WebDriver
      # or webdriver.Firefox(), webdriver.Edge(), etc.
    print("ChromeDriver path:", driver.service.path)
    print("ChromeDriver path:", driver.capabilities)
    # Your test code here...

finally:
    # Clean up
    driver.quit()
