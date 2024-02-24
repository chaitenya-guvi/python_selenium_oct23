from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class FindByLinkText():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        sleep(2)
        webelement_ByLinkText = driver.find_element(By.LINK_TEXT,"HOME")

        if webelement_ByLinkText is not None:
            print("We found an home element by Link Text")

        webelement_ByLinkText.click()
        print(driver.title)
        print(driver.current_url)

        webelement_ByLinkText = driver.find_element(By.LINK_TEXT, "BLOG")

        if webelement_ByLinkText is not None:
            print("We found blog element by Link Text")

        webelement_ByLinkText.click()
        print(driver.title)
        print(driver.current_url)


ff = FindByLinkText()
ff.test()