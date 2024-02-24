from selenium import webdriver

url = "https://www.google.com/"


driver = webdriver.Chrome()

# Open the webpage to url
driver.get(url)

# get the title of webpage
print(driver.title)