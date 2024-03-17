from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BrowserInteractions():

    def test(self):
        """
        1. opening google
        2. opening amazon on the same page

        :return:
        current url
        refresh

        """

        driver = webdriver.Firefox()
        url1 = "https://www.google.com/"
        url2 = "https://www.amazon.com/"
        # open the website google .com
        driver.get(url1)
        sleep(5)

        # maximize the window :
        driver.maximize_window()

        # go to website amazon.com
        driver.get(url2)
        title_of_page = driver.title # amazon.com
        print(f"the title of page is : " + title_of_page) # amazon.com
        sleep(5)

        # go  back to previous page
        driver.back() # google .com
        # print the title of the website
        title_of_page = driver.title
        print(f"line 38 , the title of page is : " + title_of_page) # google
        sleep(5)
        #go forward to the page
        driver.forward() # amazon.com shows on screen
        # driver.forward()  # error since ther is no forward into

        driver.refresh()
        sleep(5)
        driver.quit()

chrometest1 = BrowserInteractions()
chrometest1.test()
