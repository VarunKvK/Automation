import time
from selenium.webdriver.common.by import By

class SearchByUser:
    def __init__(self,driver):
        self.driver=driver
        self.search_btn=(By.XPATH,"//a[@titel='Search']")
        self.search_input=(By.XPATH,"//*[@id='__next']/div[3]/div/div/input")
    
    def click_search(self):
        time.sleep(4)
        self.driver.find_element(*self.search_btn).click()
    
    def search_input_value(self,search_input):
        time.sleep(4)
        self.driver.find_element(*self.search_input).send_keys(search_input)
        
    