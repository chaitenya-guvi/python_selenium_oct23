""" xpath - "https://www.guru99.com/xpath-selenium.html#7" """


"""
//tag[@attribute='value']
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


"""
identify using xpath
"""


url = "https://www.instagram.com/"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
sleep(3)

#maximise window
driver.maximize_window()

#title of page
print(driver.title)


webelement_of_email_input = driver.find_element(By.XPATH,"//input[@name='username']")
webelement_of_email_input.send_keys("999999999")

#
webelement_of_password_input = driver.find_element(By.XPATH,'//input[@type="password"]')
webelement_of_password_input.send_keys("examplepassword")

sleep(2)

xpath_of_login_button = '//button[@type="submit"]'
webelement_of_login_button= driver.find_element(By.XPATH,xpath_of_login_button)
webelement_of_login_button.click()


