from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
url = "https://qavbox.github.io/demo/signup/"

driver.get(url)

sleep(2)

# identifying the element full name using id
webelement_of_fullname_using_id = driver.find_element(By.ID,"username")
print("i have found the element full name using ID locator")
print(f"The locator is this webelement  : {webelement_of_fullname_using_id}")


# identifying the element full name using name
webelement_of_fullname_using_name = driver.find_elements(By.NAME,"uname")
print("i have found the element full name using NAME locator")
print(f"The locator is this webelement  : {webelement_of_fullname_using_name}")


# identifying MULTIPLE elements
webelements_of_labels_using_tag_name = driver.find_elements(By.TAG_NAME,"label")
print("i have found the element full name using Tag name locator")
print(f"The locator is this webelement  : {webelements_of_labels_using_tag_name}")
print(f"The length of list is  : {len(webelements_of_labels_using_tag_name)}")
