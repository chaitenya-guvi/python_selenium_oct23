from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

"""
switching frames
1. browse practice page = https://www.letskodeit.com/practice
2. search for python in the page 
3. return the list of courses with python in the name 


FRAME : 
In the context of a web browser, a frame is a part of a web page or 
browser window which displays content independent of its container, 
with the ability to load content independently. The HTML or media 
elements in a frame may come from a web site distinct from the site providing the enclosing content.

"""


class SwitchFrame:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.letskodeit.com/practice"
        # self.url = "https://www.letskodeit.com/courses"

    def browse_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(7)

    def search_course(self,course_to_search):
        id_frame_to_switch = "courses-iframe"
        frame_webelement = self.driver.find_element(By.ID,id_frame_to_switch)

        self.driver.switch_to.frame(3)

        webelement_of_search = self.driver.find_element(By.XPATH,"//input[@id='search']")
        webelement_of_search.send_keys(course_to_search)
        sleep(3)
        webelement_of_search_icon = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        webelement_of_search_icon.click()
        sleep(8)


Obj =  SwitchFrame()
Obj.browse_url()
Obj.search_course("python")