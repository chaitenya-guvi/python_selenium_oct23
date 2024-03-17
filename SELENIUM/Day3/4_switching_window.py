from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

"""
switching windows 
a tags are for links 
"""


class Cowin:

    def __init__(self):
        self.url = "https://www.cowin.gov.in/"
        self.driver = webdriver.Chrome()
        self.FAQ_LINK_xpath = "//a[@href='/faq' and @role='button']"

    def browsecowin(self):
        """
        browse cowin page
        :return: None
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(2)

    def browseFAQpage(self):
        """
        Clicking on the FAQ page url
        :return:
        """
        # prints the current URL and saves the current window id
        print("The current URL is : " + self.driver.current_url)
        present_window_handle = self.driver.current_window_handle
        print("Line 35 ----The current handle is : " + present_window_handle)


        all_window_handles = self.driver.window_handles
        print("Line 39 ---- The list of all windows is : ")
        print(all_window_handles)
        # Clicking on faq page
        FAQ_webelement = self.driver.find_element(By.XPATH, self.FAQ_LINK_xpath)
        FAQ_webelement.click()
        sleep(6)

        # get all the active / availbale window handle
        all_window_handles = self.driver.window_handles
        print("Line 53 ---- The list of all windows is : ")
        print(all_window_handles)
        # #
        for window_tab_code in all_window_handles:
            if (window_tab_code != present_window_handle):
                print("The current URL before clicking is : " + self.driver.current_url)
                self.driver.switch_to.window(window_tab_code)
                sleep(5)
                print("The current URL after switching is : " + self.driver.current_url)
                registration_button_xpath = "//div[text()=' A. Registration ']"
                webelement_of_registration_link = self.driver.find_element(By.XPATH, registration_button_xpath)
                webelement_of_registration_link.click()
                sleep(4)
                webelement_of_registration_link.click()
                sleep(4)
                webelement_of_registration_link.click()
                sleep(4)
                webelement_of_registration_link.click()
                sleep(4)
                # self.driver.close()
                self.driver.quit()

        #


obj = Cowin()
obj.browsecowin()
obj.browseFAQpage()
