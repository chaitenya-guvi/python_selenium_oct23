from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Switch:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://the-internet.herokuapp.com/dropdown"

    def browse_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def click_on_elemental_selenium(self):
        webelement_of_link = self.driver.find_element(By.LINK_TEXT,'Elemental Selenium')
        webelement_of_link.click()
        sleep(4)
        print("The current url is  : " + self.driver.current_url)
        print("The current title is  : " + self.driver.title)

    def switch_to_elemental_selenium_window(self):
        all_window_handles = self.driver.window_handles
        print("Line 26 ---- The list of all windows is : " )
        print(all_window_handles)

        for window_tab_code in all_window_handles:
            if (window_tab_code == self.driver.current_window_handle):
                print("this is the first iteration , I am on the main window handle and there is n need to switch")
            else :
                print("The current URL before switching is : " + self.driver.current_url)
                self.driver.switch_to.window(window_tab_code)
                sleep(5)
                print("The current url after switching is   : " + self.driver.current_url)
                print("The current title after switching is   : " + self.driver.title)




abc = Switch()
abc.browse_url()
abc.click_on_elemental_selenium()
abc.switch_to_elemental_selenium_window()