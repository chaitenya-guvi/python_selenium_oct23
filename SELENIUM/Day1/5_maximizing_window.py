from selenium import webdriver
from time import sleep

url = "https://www.google.com/"
url2  = "https://www.guvi.in"

driver = webdriver.Chrome()
# method for maximizing the window
driver.maximize_window()
# Open the webpage to url
driver.get(url)

# get the title of webpage
print(driver.title)

# opening the second url
driver.get(url2)
# pauses the execution for 2 seconds
sleep(2)
print(driver.title)

# method to go back one page
driver.back()
sleep(2)
print(driver.title)


