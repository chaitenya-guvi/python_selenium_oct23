from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
"""
Description: This exception is raised when WebDriver is unable to locate an element in the DOM.
Example: Trying to find an element using 
find_element BY ID  but the specified ID doesn't exist in the HTML document.
"""


driver = webdriver.Chrome()
try:
    element = driver.find_element(By.ID,"non_existent_id")
except NoSuchElementException as e:
    print("Element not found:", e)
