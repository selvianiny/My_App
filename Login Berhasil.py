import unittest
import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variabel
url = "https://myappventure.herokuapp.com/login"
email ="selviani@gmail.com"
pswd = "selvi123"

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

# test case pertama
    def test_success_login(self):

# Membuka situs web
        driver = self.driver
        driver.get(url)
        time.sleep(3)
 # isi email       
        driver.find_element(By.NAME,"email").send_keys(email) 
        time.sleep(1)
 # isi password        
        driver.find_element(By.NAME,"password").send_keys(pswd)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(15)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()