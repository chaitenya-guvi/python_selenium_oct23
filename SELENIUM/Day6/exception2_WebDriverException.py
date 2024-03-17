"""
WebDriverException
Description: This is a general exception class for WebDriver errors
not covered by more specific exceptions.
Example: Any unexpected error during WebDriver initialization or execution.

"""

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

try:
    driver = webdriver.Firefox()
    driver.get("abcd")
except WebDriverException as e:
    print("WebDriver error:", e)
