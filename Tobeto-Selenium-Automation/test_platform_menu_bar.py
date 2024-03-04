import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from valid_login import Test_Valid_Login

class Test_Platform_Menu_Bar:
    
    def setup_method(self):

        chrome_driver_path = Service("/Users/gunesgulay/Desktop/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get(c.LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()    
  
    def test_menu_bar_ikon(self):
            
        validLoginClass = Test_Valid_Login(self.driver)
        validLoginClass.valid_login("majajiv633@vasteron.com","deneme123")
        sleep(3)  
            
        homePageButton = self.driver.find_element(By.XPATH, c.HOME_PAGE)
        homePageButton.click()
        sleep(2)

        homePageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.HOME_PAGE_CONTROLLER)))
        assert homePageController.text == "TOBETO'ya hoş geldin"
        sleep(2)
            
        myProfileButton = self.driver.find_element(By.XPATH, c.MY_PROFILE)
        myProfileButton.click()
        sleep(2)

        profileController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.MY_PROFILE_CONTROLLER)))
        assert profileController.text == "test automation"
        sleep(2)

        assessmentsButton = self.driver.find_element(By.XPATH, c.ASSESSMENTS)
        assessmentsButton.click()
        sleep(2)

        assessmentsController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.ASSESSMENTS_CONTROLLER)))
        assert assessmentsController.text == "Yetkinliklerini ücretsiz ölç, bilgilerini test et."
        sleep(2)

        catalogButton = self.driver.find_element(By.XPATH, c.CATALOG)
        catalogButton.click()
        sleep(2)

        catalogController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.CATALOG_CONTROLLER)))
        assert catalogController.text == "Öğrenmeye başla !"
        sleep(2)

        calendarButton = self.driver.find_element(By.XPATH, c.CALENDAR)
        calendarButton.click()
        sleep(2)

        calendarController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.CALENDAR_CONTROLLER)))
        assert calendarController.text == "Bugün"
        sleep(2)
            
        istanbulCodingButton = self.driver.find_element(By.XPATH, c.ISTANBUL_CODING)
        istanbulCodingButton.click()
        sleep(2)

        istanbulCodingController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.ISTANBUL_CODING_CONTROLLER)))
        assert istanbulCodingController.text == "Aradığın  “İş”  Burada!"
        sleep(2)


            