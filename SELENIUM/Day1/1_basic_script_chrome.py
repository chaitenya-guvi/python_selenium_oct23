from selenium import webdriver

url = 'https://www.guvi.in'

# automation with firefox browser
driver = webdriver.Chrome()

# this method opens the url passed
driver.get(url)

