from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from selenium.webdriver.chrome.options import Options as ChromeOptions


class LoginTest(unittest.TestCase):
    def setUp (self):
        opts = ChromeOptions()
        opts.add_argument('--headless')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        opts.binary_location = "/usr/bin/google-chrome"

        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=opts)
        self.driver.get("http://127.0.0.1/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_login_valid (self):
        self.driver.find_element_by_name("email").send_keys("mm@gmail.com")
        self.driver.find_element_by_name("password").send_keys("MM@3841")
        self.driver.find_element_by_id("submit-login").click()
        self.driver.find_element_by_class_name("logout").click()
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()
        print("Test completed")
        
if __name__== '__main__':

    unittest.main()
