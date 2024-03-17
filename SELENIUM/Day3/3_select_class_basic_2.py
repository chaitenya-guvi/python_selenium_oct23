from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class  DropdownExample2():

    def  test1(self):

        baseurl = "https://www.letskodeit.com/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()
        driver.get(baseurl)


        id_to_carselect_dropdown = 'carselect'
        webelement_of_select_class = driver.find_element(By.ID,id_to_carselect_dropdown)
        time.sleep(4)
        sel = Select(webelement_of_select_class)

        # select ing by value
        sel.select_by_value("honda")
        time.sleep(5)
        #
        # # selecting by index
        sel.select_by_index(0)
        time.sleep(5)
        #
        #
        # # selecting by text
        sel.select_by_visible_text("Benz")
        time.sleep(5)
        #
        # # selecting by index - 2
        sel.select_by_index("1")

        driver.quit()


ff = DropdownExample2()
ff.test1()
