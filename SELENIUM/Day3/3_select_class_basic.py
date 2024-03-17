from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
## import select class
from selenium.webdriver.support.select import Select


class DropdownSelect():

    def test(self):
        """
        Select class - only interactable with select tag
        select by : -index  -------
                    - value
                    - visible text

        :return:
        """

        baseUrl = "https://the-internet.herokuapp.com/dropdown"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        # driver.implicitly_wait(10)
        sleep(5)

        id_to_dropdown = "dropdown"
        webelement_of_dropdown = driver.find_element(By.ID,id_to_dropdown)

        # passed web elements in the select class as an argument to select class
        sel = Select(webelement_of_dropdown)
        sleep(5)
        #Returns a list of all options belonging to this select tag
        print(sel.options)
        #iterating over web elements list and printing the text of options
        for list_options in sel.options :
            print(list_options.text)
        driver.quit()

ff = DropdownSelect()
ff.test()