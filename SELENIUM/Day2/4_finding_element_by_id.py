from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


"""
identify using id
"""


url = "https://www.instagram.com/"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
sleep(2)

#maximise window
driver.maximize_window()

#title of page
print(driver.title)


webelement_of_email_input = driver.find_element(By.ID,"email")
webelement_of_email_input.send_keys("999999999")


webelement_of_password_input = driver.find_element(By.ID,"pass")
webelement_of_password_input.send_keys("examplepassword")

