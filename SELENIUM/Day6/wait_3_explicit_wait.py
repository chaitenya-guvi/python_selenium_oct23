"""
Explicit waits in Selenium are used to wait
for a certain condition to occur before
proceeding with the execution of
the next steps in the automation script.


This can be particularly useful when dealing with dynamic web elements
that may take some time to load or change state.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize Firefox WebDriver
driver = webdriver.Firefox()
driver.maximize_window()

# Open OrangeHRM demo website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Define an explicit wait with a maximum timeout of 10 seconds
wait = WebDriverWait(driver, 10,poll_frequency=1)

# Wait until the username field is visible and can be interacted with

username_field_webelement = wait.until(EC.visibility_of_element_located((By.NAME, "username")))

# Enter username
username_field_webelement.send_keys("Admin")

# Wait until the password field is visible and can be interacted with
password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))

# Enter password
password_field.send_keys("admin123")

# Wait until the login button is clickable
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))

# Click the login button
login_button.click()



# Close the browser
driver.quit()
