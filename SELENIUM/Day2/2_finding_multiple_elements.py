from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
sleep(2)
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
driver.find_elements(Locator , Locator value ) 
returns a list of elements 
"""

webelement_of_login_button = driver.find_element(By.TAG_NAME,"button")
# print(webelement_of_login_button)
webelement_of_login_button.click()

"find elements will return a list ,empty list of elemnt is not found"
webelements_of_input_tags = driver.find_elements(By.TAG_NAME,"input")
print(len(webelements_of_input_tags))
print(webelements_of_input_tags)

webelements_of_input_tags = driver.find_elements(By.TAG_NAME,"a")
print(len(webelements_of_input_tags))
print(webelements_of_input_tags)
