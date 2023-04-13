import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Login_User_with_Right_credential(self):
        driver = self.driver
        driver.get("http://localhost:3000")
        elem = driver.find_element(By.ID, "Email")
        password = driver.find_element(By.ID, "password")
        button= driver.find_element(By.CLASS_NAME, "SubmitButton")
        print(elem)
        elem.send_keys("test@test.com")
        password.send_keys('test')
        password.send_keys(Keys.RETURN)
        print(driver.current_url)
        time.sleep(0.5)
        self.assertIn("Getting started", driver.find_element(By.CLASS_NAME, "landing__header"))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()