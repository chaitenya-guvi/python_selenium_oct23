from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

"""
 wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,
                                                         "stopFilter_stops-0")))

1. Go to internet heroku dynamic loading page
2. Click the example 1 
3. Click the start button 
4. wait till "hello world is printed "
5. printing the time that we have waited for --- utilising the time module                                                          

"""


class ExplicitExample():

    def test(self):
        driver = webdriver.Chrome()

        # Defing url
        url_omayo4 = "http://omayo.blogspot.com/"
        url_letskodeit = "https://courses.letskodeit.com/practice"
        url_internet_heroku = "https://the-internet.herokuapp.com/dynamic_loading"

        # open the webpage
        driver.get(url_internet_heroku)

        # maximize the window
        driver.maximize_window()

        # defining webdriver wait wait
        wait_2 = WebDriverWait(driver, 10)
        wait3 = WebDriverWait(driver, 10, 1)

        wait_for_element1 = WebDriverWait(driver, 10, 1,
                                          ignored_exceptions=[NoSuchElementException,
                                                              ElementNotVisibleException,
                                                              ElementNotSelectableException,
                                                              ElementNotInteractableException,
                                                              TimeoutException])

        example_1_xpath = "//a[@href='/dynamic_loading/1']"
        example_1_element = driver.find_element(By.XPATH, example_1_xpath)
        example_1_element.click()

        title_element = wait_for_element1.until(EC.title_contains("Internet"))
        print("The value of title contains check is  : " + str(title_element))

        start_id = "//div[@id='start']//button"
        finish_id = "finish"
        # click the start element
        start_element = driver.find_element(By.XPATH, start_id)
        time.sleep(1)
        start_element.click()
        # notes the time of start of our script

        print(time.time())

        finish_element = wait_for_element1.until(EC.element_to_be_clickable((By.ID, finish_id)))
        # notes the time of end of our script
        print(time.time())

        time.sleep(4)
        driver.quit()


go = ExplicitExample()
go.test()