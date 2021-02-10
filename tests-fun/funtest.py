from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import unittest
from selenium.webdriver.chrome.options import Options as ChromeOptions
import xmlrunner

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        opts = ChromeOptions()
        opts.add_argument('--headless')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        opts.binary_location = "/usr/bin/google-chrome"

        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=opts)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        #self.driver.save_screenshot("toto.png")
        
    def test_create_login (self):
        self.driver.get("http://10.10.20.76:8001/login?back=my-account")
        self.driver.find_element_by_name("email").send_keys("bb@gmail.com")
        self.driver.find_element_by_name("password").send_keys("BB@3841")
        self.driver.find_element_by_partial_link_text("No account?").click()
        self.driver.find_element_by_name("id_gender").send_keys("2")
        self.driver.find_element_by_name("firstname").send_keys("test")
        self.driver.find_element_by_name("lastname").send_keys("test")
        self.driver.find_element_by_name("email").send_keys("bb@gmail.com")
        self.driver.find_element_by_name("password").send_keys("BB@1234")
        self.driver.find_element_by_name("optin").send_keys("1")
        self.driver.find_element_by_name("newsletter").send_keys("1")
        self.driver.find_element_by_name("psgdpr").send_keys("1")
        self.assertIn("Create an account", self.driver.page_source)
        self.driver.find_element_by_class_name("btn-primary").click()
        time.sleep(2)
        
    #def test_login_valid (self):
    #    self.driver.get("http://10.10.20.76:8001/login?back=my-account")
    #    self.driver.find_element_by_name("email").send_keys("mm@gmail.com")
    #    self.driver.find_element_by_name("password").send_keys("MM@3841")
    #    self.driver.find_element_by_id("submit-login").click()
    #    self.assertNotIn("Authentication failed.", self.driver.page_source)
    #    self.driver.find_element_by_class_name("logout").click()
    #    time.sleep(2)
        
    def test_search_page (self):
        search_query = "mug"
        self.driver.get("http://10.10.20.76:8001/")
        self.driver.find_element_by_name("s").send_keys(search_query)
        #self.driver.find_element_by_class_name("material-icons").click()
        self.driver.find_element_by_xpath("//button").click()
        self.driver.find_elements_by_id("js-product-list")
        results = self.driver.find_elements_by_class_name("product-miniature")
        self.assertTrue(results)
        #for article in results:
        #    print(article.text)
        #    print()
    
    def tearDown(self):
        self.driver.quit()
        print("Test completed")

if __name__== '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'))
    
