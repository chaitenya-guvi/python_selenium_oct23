from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class ActionChainsDragExample:
    url = 'https://qavbox.github.io/demo/dragndrop/'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Create the ActionChains Object which will take webdriver as an argument
    action = ActionChains(driver)
    # Locators for draggable and target object
    source_1 = 'draggable'
    target_1 = 'droppable'

    # Browsing Method
    def browsing(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def move_slider(self):
        sleep(2)
        xpath_of_slider = '//input[@type="range"]'
        webelement_slider = self.driver.find_element(By.XPATH, xpath_of_slider)
        self.action.drag_and_drop_by_offset(webelement_slider, 50, 0).perform()
        sleep(4)
        self.action.drag_and_drop_by_offset(webelement_slider, -20, 0).perform()
        sleep(4)


obj = ActionChainsDragExample()
obj.browsing()
obj.move_slider()
