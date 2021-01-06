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

    def test_login (self):
        psEmail = 'mm@gmail.com'
        psPassword = 'MM@3841'
        emailFieldName = 'email'
        passFieldName = 'password'
        loginButtonXpath = '//input[@value="my-account"]'
        logoXpath = '//a[@rel="nofollow"]'
        driver = self.driver

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver:find_element_by_name(emaiFieldName))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver:find_element_by_name(passFieldName))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver:find_element_by_xpath(logoXpath))
        
        emailFieldElement.clear()
        emailFieldElement.send_keys(psEmail)
        passFieldElement.clear()
        passFieldElement.send_keys(psPassword)
        loginButtonElement.click()

        webDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath())

    def tearDown(self):
        self.driver.quit()

if __name__== '__main__':

    unittest.main()
