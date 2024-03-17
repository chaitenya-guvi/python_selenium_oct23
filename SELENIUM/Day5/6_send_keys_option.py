from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class SendKeysExample:
    def __init__(self):
        # Open Facebook login page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com")

    def credenrials_browse(self):
        # Find email and password fields and enter credentials
        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys("your_email@example.com")

        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys("your_password")

        # Simulate pressing Enter to submit the form
        password_field.send_keys(Keys.ENTER)

        # Wait for the login process to complete
        sleep(10)

        # Check if login was successful

        # Close the browser
        self.driver.quit()

obj = SendKeysExample()
obj.credenrials_browse()