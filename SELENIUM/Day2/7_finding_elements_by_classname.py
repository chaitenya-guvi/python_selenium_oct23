from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



driver = webdriver.Firefox()

url = "https://www.letskodeit.com/practice"

driver.get(url)


driver.maximize_window()

sleep(2)


webelements_of_left_align_class = driver.find_elements(By.CLASS_NAME, "left-align")
print(webelements_of_left_align_class)
print(len(webelements_of_left_align_class))

for element in webelements_of_left_align_class :
    print(element.get_attribute("id"))


