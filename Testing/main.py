import time
import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from login import Login

load_dotenv()

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)
@pytest.fixture
def driver():
    driver = webdriver.Chrome(chrome_opt)  # Initialize WebDriver instance
    yield driver  # Provide the WebDriver instance to the test functions

def test_example_user_login(driver):
    login_page=Login(driver=driver)
    driver.get("https://savee.it") #Link to Automate testing

    login_page.click_login_cta() #Click login cta to register as a new user

    #Enter the credentials
    login_page.enter_username(os.getenv("EMAIL"))
    login_page.enter_password(os.getenv("PASSWORD"))
    
    login_page.click_login() #Click login
    