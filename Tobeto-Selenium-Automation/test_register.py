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

class Test_Register:

    def setup_method(self):

        chrome_driver_path = Service("/Users/gunesgulay/Desktop/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get(c.LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self):
        
        self.driver.quit()  

    def register(self, email, password1, password2, phone):

        firstRegisterButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.FIRST_REGISTER_BUTTON)))
        firstRegisterButton.click()

        nameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.NAME_NAME)))
        nameInput.send_keys("test")

        surnameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.SURNAME_NAME)))
        surnameInput.send_keys("automation")

        enterEmail = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.ENTER_EMAIL)))
        enterEmail.send_keys(email)

        enterPassword = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.ENTER_PASSWORD)))
        enterPassword.send_keys(password1) 

        passwordAgain = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_AGAIN)))
        passwordAgain.send_keys(password2) 
        sleep (5)

        registerButton = WebDriverWait(self.driver, 35).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_BUTTON_XPATH)))
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep (5)
        registerButton.click()

        explicitConsentStatementCheckbox = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.EXPLICIT_CONSENT_CHECKBOX)))
        explicitConsentStatementCheckbox.click()

        membershipContratCheckbox = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.MEMBERSHIP_CONTRAT_CHECKBOX)))
        membershipContratCheckbox.click()

        emailConfirmationCheckbox = self.driver.find_element(By.NAME,c.EMAIL_CONFIRMATION_CHECKBOX)
        emailConfirmationCheckbox.click()

        phoneConfirmationCheckbox = self.driver.find_element(By.NAME,c.PHONE_CONFIRMATION_CHECKBOX)
        phoneConfirmationCheckbox.click()

        enterPhone = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,c.ENTER_PHONE)))
        enterPhone.send_keys(phone)

        iframe = self.driver.find_element(By.XPATH,c.IFRAME_XPATH)
        self.driver.switch_to.frame(iframe)
        sleep (2)

        reCAPTCHA = self.driver.find_element(By.XPATH, c.RECAPTCHA_CHECKBOX)
        reCAPTCHA.click()
        sleep (20)

        self.driver.switch_to.default_content()

        continueButton = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH,c.CONTINUE_BUTTON_XPATH)))
        continueButton.click()

    def test_successful_register(self):

        self.register("testautomation87@outlook.com", "deneme123", "deneme123", "5068414863")
        sleep (5)

        registerMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.REGISTER_MESSAGE)))
        assert "Tobeto Platform'a kaydınız başarıyla gerçekleşti." in registerMessage.text 
 
    def test_invalid_email(self):

        firstRegisterButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.FIRST_REGISTER_BUTTON)))
        firstRegisterButton.click()

        enterEmail = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.ENTER_EMAIL)))
        enterEmail.send_keys("testautomation652@")
        
        invalidEmailMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.INVALID_EMAIL_MESSAGE)))
        assert invalidEmailMessage.text == "Geçersiz e-posta adresi*"    

    def test_invalid_phone_message(self):

        self.register("testautomation652@gmail.com", "deneme123", "deneme123", "1234")

        invalidPhoneMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.INVALID_PHONE_MESSAGE)))
        assert invalidPhoneMessage.text == "En az 10 karakter girmelisiniz."
        sleep (5)

    def test_invalid_phone_message2(self):

        self.register("testautomation1@gmail.com", "deneme123", "deneme123", "12345678987")

        invalidPhoneMessage2 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.INVALID_PHONE_MESSAGE2)))
        assert invalidPhoneMessage2.text == "En fazla 10 karakter girebilirsiniz."    
        sleep (5)

    def test_registered_email(self):
        
        self.register("dojogij877@wikfee.com", "deneme123", "deneme123", "5068372511")

        errorMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.CLASS_NAME,c.REGISTERED_EMAIL_MESSAGE)))
        assert errorMessage.text == "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."
        sleep(5)  
    
    def test_password_less_6(self):
        
        self.register("testautomation65@gmail.com", "test4", "test4", "5068372511")

        errorMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.CLASS_NAME, c.PASSWORD_ERROR_MESSAGE)))
        assert errorMessage.text == "• Şifreniz en az 6 karakterden oluşmalıdır."
        sleep(5)

    def test_non_matching_passwords(self):
        
        self.register("testautomation99@gmail.com", "test4", "test5", "5068372511")

        errorMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.CLASS_NAME, c.NON_MATCHING_PASSWORDS)))
        assert errorMessage.text == "• Şifreler eşleşmedi"
        sleep(5)    
    
    def test_two_errors(self):
        
        self.register("test456@hotmail.com", "test4", "test4", "5068372511")

        errorMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.CLASS_NAME, c.TWO_ERRORS_MESSAGE)))
        assert errorMessage.text == "• 2 errors occurred"
        sleep(5)        