from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import unittest
from selenium.webdriver.chrome.options import Options as ChromeOptions


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        opts = ChromeOptions()
        opts.add_argument('--headless')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        opts.binary_location = "/usr/bin/google-chrome"

        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=opts)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.save_screenshot("toto.png")

    def test_login_valid (self):
        self.driver.get("http://10.10.20.71/fr/connexion?back=my-account")
        self.driver.find_element_by_name("email").send_keys("mm@gmail.com")
        self.driver.find_element_by_name("password").send_keys("MM@3841")
        self.driver.find_element_by_id("submit-login").click()
        self.driver.find_element_by_class_name("logout").click()
        time.sleep(2)
		
	def test_search_page (self):
#               wait = WebDriverWait(self.driver, 10)
               search_query = "mug"
               self.driver.get("http://10.10.20.71/")
               self.driver.find_element_by_name("s").send_keys(search_query)
               self.driver.find_element_by_class_name("material-icons").click()
#               wait.until(presence_of_element_located((By.ID, "js-product-list")))
               self.driver.find_elements_by_id("js-product-list")
               #results
               results = self.driver.find_elements_by_class_name("product-miniature")
               for article in results:
                   print(article.text)
                   print()
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("Test completed")

if __name__== '__main__':

    unittest.main()
