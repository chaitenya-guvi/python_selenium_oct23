from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
url = "https://www.instagram.com/"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
sleep(4)
"""
task is to open orange hrm website 
and input some txt in the username field
"""

"""
1. identify the element  through selenium
2 . then perform an action on element
"""

"""
The method name for finding 
single element - find_element
multiple elements - find_elements
"""

"""
driver.find_element(Locator , Locator value ) 
"""
# finding elements by name
webelement_of_username_input = driver.find_element(By.NAME,"username")
webelement_of_password_input = driver.find_element(By.NAME,"password")



"send text for the element - requirement for this is the leemnt should be an input tag"

webelement_of_username_input.send_keys("Admin")
webelement_of_password_input.send_keys("admin123")

# # finding by Tag name
# webelement_of_login_button = driver.find_element(By.TAG_NAME,"button")
# # print(webelement_of_login_button)
# webelement_of_login_button.click()



