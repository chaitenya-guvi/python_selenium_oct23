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

    # ActionChains Drag and Drop Offset
    def drag_drop_offset(self):
        sleep(5)
        source_1 = self.driver.find_element(by=By.ID, value=self.source_1)
        target_1 = self.driver.find_element(by=By.ID, value=self.target_1)
        # moving horizontally
        self.action.drag_and_drop_by_offset(source_1, xoffset=200, yoffset=0).perform()
        sleep(5)
        self.action.drag_and_drop_by_offset(source_1, -200, 0).perform()
        sleep(5)
        # moving vertically
        self.action.drag_and_drop_by_offset(source_1, 0, 50).perform()
        sleep(5)
        self.action.drag_and_drop_by_offset(source_1, 0, -100).perform()


obj = ActionChainsDragExample()
obj.browsing()
obj.drag_drop_offset()
