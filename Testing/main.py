import time
import os
from dotenv import load_dotenv
import pytest
import pytest_dependency
from selenium import webdriver
from selenium.webdriver.common.by import (By)

load_dotenv()

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)
@pytest.fixture
def driver():
    driver = webdriver.Chrome(chrome_opt)  # Initialize WebDriver instance
    yield driver  # Provide the WebDriver instance to the test functions
    # driver.quit()  # Teardown: Quit the WebDriver after the tests

def test_example(driver):
    driver.get("https://savee.it/")
    driver.find_element(By.XPATH,"//a[@title='Log in']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/form/div[1]/input').send_keys(os.getenv("EMAIL"))
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[2]/form/div[2]/input').send_keys(os.getenv("PASSWORD"))
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@title='Log in']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/ul/li[3]/ul/li[4]/div/a/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div[2]/div[2]/div[2]/ul/li[2]/div/div/a').click()
    
# def test_get_to_profile(driver):
#     driver.get("https://savee.it/")
#     time.sleep(2)
#     driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/ul/li[3]/ul/li[4]/div/a/span').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div[2]/div[2]/div[2]/ul/li[2]/div/div/a').click()