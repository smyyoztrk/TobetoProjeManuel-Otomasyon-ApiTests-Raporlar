import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Test_Calendar:
    def setup_method(self):

        chrome_driver_path = Service("/Users/gunesgulay/Desktop/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get(c.LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  
  
    def test_calendar_login(self):

        calendar = self.driver.find_element(By.CLASS_NAME, c.CALENDAR_CLASS)
        calendar.click()

        calendarController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.CALENDAR_CONTROLLER)))
        sleep (15)
        assert calendarController.text == "Bugün"
        sleep(3)
    
    def test_calendar_out(self):

        self.test_calendar_login()
        sleep(3)
        calendar_out = self.driver.find_element(By.XPATH, c.CALENDAR_OUT)
        calendar_out.click()
        sleep(3)

        calendar = self.driver.find_element(By.CLASS_NAME, c.CALENDAR_CLASS)
        