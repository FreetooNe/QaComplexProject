import logging
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegisterUser:
    log = logging.getLogger("[Register form NEW user: ]")

    """
           -Description: Positive TEST 
           - Pre-conditions:
               1 - Open start page
           - Steps:
               2 - Fill username
               3 - Fill Email
               4 - Fill password
               5 - Click on button "Sign up for OurApp"
               5 - Verify error
           """

    def test_start_page(self):
        # STEP 1 - Open start page
        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        driver.maximize_window()
        print(" ========= Positive TEST ========= ")
        self.log.info("Start page was opened")
        sleep(1)

        # STEP 2 - Fill username
        user_name_field = driver.find_element(by=By.XPATH, value=".//input[@id = 'username-register']")
        user_name_field.clear()
        user_name_field.send_keys(f"Dima{randint(0, 1000)}")
        self.log.info("Username has been entered")

        # STEP 3 - Fill random EMAIL
        user_email_field = driver.find_element(by=By.XPATH, value=".//input[@id = 'email-register']")
        user_email_field.clear()
        user_email_field.send_keys(f"TestEmail{randint(0, 1000)}@gmail.com")
        self.log.info("Email has been entered")

        #  STEP 4 - Fill random password
        user_password_field = driver.find_element(by=By.XPATH, value=".//input[@id = 'password-register']")
        user_password_field.clear()
        user_password_field.send_keys(f"{randint(1000000000000, 10000000000000)}")
        self.log.info("Password has been entered")

        # STEP 5 - Click on button "Sign up for OurApp"
        sign_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sign_button.click()
        sleep(5)
        sign_button.click()
        self.log.info("The button has been pressed")

        # find button Sign_Out
        sign_out = driver.find_element(by=By.XPATH, value=".//button[@class = 'btn btn-sm btn-secondary']")
        self.log.info("Button sign out was found")

        # check for button Sign_Out
        assert sign_out, f"Button Sign_Out not found {sign_out}"

        driver.close()

        """
                   -Description: Checking for validation of the email field 
                   - Pre-conditions:
                       1 - Open start page
                   - Steps:
                       2 - Fill email
                       3 - Verify error
                   """

        # STEP 1 - Open start page
        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        driver.maximize_window()
        print(" =========  TEST - Checking for validation of the email field ========= ")
        self.log.info("Start page was opened")
        sleep(1)

        # STEP 2 - Fill incorrect email
        field_incorrect_email = driver.find_element(by=By.XPATH, value=".//input[@id = 'email-register']")
        field_incorrect_email.clear()
        field_incorrect_email.send_keys(f"TestEmail{randint(0, 1000)}")
        self.log.info("Incorrect email was entered")

        # STEP 3 - found validation massage
        validation_massage_email = driver.find_element(by=By.XPATH, value="//*[@id='registration-form']/div[2]/div")
        self.log.info("validation massage was found")

        # check for button Sign_Out
        assert validation_massage_email

        driver.close()

        """
                          -Description: Checking for validation of the password field 
                          - Pre-conditions:
                              1 - Open start page
                          - Steps:
                              2 - Fill email
                              3 - Verify error
                          """

        # STEP 1 - Open start page
        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        driver.maximize_window()
        print(" =========  TEST - Checking for validation of the password field ========= ")
        self.log.info("Start page was opened")
        sleep(1)

        # STEP 2 - Fill password not more then 12 symbols
        user_password_field = driver.find_element(by=By.XPATH, value=".//input[@id = 'password-register']")
        user_password_field.clear()
        user_password_field.send_keys(f"{randint(100, 10000)}")
        self.log.info("Incorrect Password has been entered")

        # STEP 3 - Verify validation_massage
        validation_massage_password = driver.find_element(by=By.XPATH, value='//*[@id="registration-form"]/div[3]/div')
        self.log.info("Verify massage was found")

        # check for button Sign_Out
        assert validation_massage_password

        driver.close()
