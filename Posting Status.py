import unittest
import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.url = webdriver.Chrome(ChromeDriverManager().install())

    def test_posting(self): 
# steps
        url = self.url #buka situs posting
        url.get("https://myappventure.herokuapp.com/upload") # buka situs update
        time.sleep(3)
 #Isi kolom posting       
        url.find_element(By.XPATH,"/html/body/div/main/div/div/div/div[2]/form/div/label/textarea").send_keys("selamat belajar") 
        time.sleep(1)
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()