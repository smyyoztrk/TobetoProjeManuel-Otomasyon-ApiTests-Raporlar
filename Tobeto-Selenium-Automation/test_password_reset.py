from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import openpyxl
from time import sleep
from constants import globalConstants as c

class Test_Password_Reset:

    def setup_method(self):

        chrome_driver_path = Service("/Users/gunesgulay/Desktop/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get(c.LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  

    def test_successful_password_reset(self):
        
        resetButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_RESET_BUTTON)))
        resetButton.click()

        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SIGN_UP_MAIL_XPATH)))
        emailInput.send_keys("test456@hotmail.com")

        sendButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SEND_BUTTON_XPATH)))
        sendButton.click()

        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SYSTEM_MESSAGE_XPATH)))
        assert systemMessage.text == "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
    
    def test_unsuccessful_password_reset(self):

        resetButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_RESET_BUTTON)))
        resetButton.click()

        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SIGN_UP_MAIL_XPATH)))
        emailInput.send_keys("@hotmail.com")

        sendButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.SEND_BUTTON_XPATH)))
        sendButton.click()

        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, c.ERROR_MESSAGE)))
        assert errorMessage.text == "• Girdiğiniz e-posta geçersizdir."    