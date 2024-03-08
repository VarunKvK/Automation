from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.driver=driver
        self.login_cta=(By.XPATH,"//a[@title='Log in']")
        self.username=(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/form/div[1]/input')
        self.password=(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/form/div[2]/input')
        self.login_btn=(By.XPATH,"//button[@title='Log in']")
    
    def click_login_cta(self):
        self.driver.find_element(*self.login_cta).click()
    
    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)
    
    
    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)
        
    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
        