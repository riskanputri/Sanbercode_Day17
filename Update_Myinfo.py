import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class day17(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def testing_MyInfo(self):
        #Update My Info(Positive Case)
        
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)

        #My_Info
        web.find_element(By.LINK_TEXT,"My Info").click()
        time.sleep(3)
        
        #First_name
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Mrs.")

        #Middle_name
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("Riska Nurhana")
        
        #Last_name
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Putri")
        
        #Nickname
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("Riskanputris")
      
        #save
        web.find_element(By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
        time.sleep(6)

        #Validation
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
