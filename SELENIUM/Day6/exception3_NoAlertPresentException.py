"""
8. NoAlertPresentException
Description: This exception is raised when WebDriver tries to switch to an alert but no alert is present.
Example: Attempting to switch to an alert when there is no alert on the page.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Firefox()

try:
    alert = driver.switch_to.alert
except NoAlertPresentException as e:
    print("No alert present:", e)
