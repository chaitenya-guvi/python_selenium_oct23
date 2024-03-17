"""
there are 2 types of waits
 - implicit wait
 - explicit wait ( exceptions )
"""


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)

# sleep(2)  # please wait for 2 seconds . , just to have a wait time for screen loads

username = 'Admin'
password = 'admin123'
    # Locators for Login
username_locator = 'username'
password_locator = 'password'

submitButton_locator = '//button[@type="submit"]'

webelemnt_of_username = driver.find_element(By.NAME,username_locator)
webelemnt_of_password = driver.find_element(By.NAME,password_locator)
webelemnt_of_submitButton= driver.find_element(By.XPATH,submitButton_locator)


webelemnt_of_username.send_keys(username)
webelemnt_of_password.send_keys(password)
webelemnt_of_submitButton.click()


# sleep(2)
Admin_menu_option_xpath = '//a[@href="/web/index.php/admin/viewAdminModule"]'
Admin_menu_option_webelement = driver.find_element(By.XPATH,Admin_menu_option_xpath)

Admin_menu_option_webelement.click()

