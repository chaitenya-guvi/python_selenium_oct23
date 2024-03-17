from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

"""
switching frames
1. browse practice page = https://www.letskodeit.com/practice
2. search for python in the page 
3. return the list of courses with python in the name 


Nested FRAME : 
frame within a frame

"""


class SwitchFrame:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://the-internet.herokuapp.com/nested_frames"

    def browse_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def search_middle_frame(self):
        # switching to top frame
        xpath_frame_top_switch = "//frame[@name='frame-top']"
        top_frame_webelement = self.driver.find_element(By.XPATH, xpath_frame_top_switch)
        self.driver.switch_to.frame(top_frame_webelement)

        sleep(1)

        # switching to middle frame within top frame
        xpath_frame_to_switch = "//frame[@name='frame-middle']"
        middle_frame_webelement = self.driver.find_element(By.XPATH,xpath_frame_to_switch)

        self.driver.switch_to.frame(middle_frame_webelement)

        webelement_of_middle_text = self.driver.find_element(By.ID,"content")
        print("This is the content in middle frame : ")
        print(webelement_of_middle_text.text)


Obj =SwitchFrame()
Obj.browse_url()
Obj.search_middle_frame()