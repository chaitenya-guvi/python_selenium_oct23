from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



driver = webdriver.Firefox()

url = "https://www.letskodeit.com/practice"

driver.get(url)

driver.maximize_window()

# webelement_of_radio_button_bmw_input = driver.find_element(By.NAME,"cars")
webelements_of_radio_button_bmw_input = driver.find_elements(By.NAME,"cars")
print(len(webelements_of_radio_button_bmw_input))

for ele in webelements_of_radio_button_bmw_input :
    print(ele.get_attribute("id"))
    print(ele.get_attribute("type"))
    print(ele.get_attribute("value"))
    print("0-0-"*10)




