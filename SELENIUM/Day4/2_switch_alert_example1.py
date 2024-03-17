from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

"""
switching frames
1. browse practice page = https://www.letskodeit.com/practice
2. click for alert button 
3. accept the alert




"""


class AlertHandle:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://www.letskodeit.com/practice"
        # self.url = "https://www.letskodeit.com/courses"

    def browse_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def generate_alert(self):
        id_of_alert_button  = "alertbtn"
        alert_button_webelement = self.driver.find_element(By.ID,id_of_alert_button)
        alert_button_webelement.click()
        sleep(3)

    def switch_to_alert(self):
        print("before accepting the alert")
        sleep(3)
        alert1 = self.driver.switch_to.alert
        alert1.accept()
        sleep(3)
        print(" print after accepting the alert")
        sleep(3)


Obj =  AlertHandle()
Obj.browse_url()
Obj.generate_alert()
Obj.switch_to_alert()