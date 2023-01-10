import logging
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegisterUser:
    log = logging.getLogger("[Register form NEW user: ]")

    """
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
        """STEP 1 - Open start page"""
        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        driver.maximize_window()
        self.log.info("Start page was opened")
        sleep(1)

        """ STEP 2 - Fill username """
        user_name_field = driver.find_element(by=By.XPATH, value=".//input[@id = 'username-register']")
        user_name_field.clear()
        user_name_field.send_keys(f"Dima{randint(0, 1000)}")
        self.log.info("Username has been entered")

        """ STEP 3 - Fill random EMAIL """
        user_email_field = driver.find_element(by=By.XPATH, value=".//input[@id = 'email-register']")
        user_email_field.clear()
        user_email_field.send_keys(f"TestEmail{randint(0, 1000)}@gmail.com")
        self.log.info("Email has been entered")

        """ STEP 4 - Fill random password """
        user_password_field = driver.find_element(by=By.XPATH, value=".//input[@id = 'password-register']")
        user_password_field.clear()
        user_password_field.send_keys(f"{randint(1000000000000, 10000000000000)}")
        self.log.info("Password has been entered")

        """ STEP 5 - Click on button "Sign up for OurApp" """
        sign_button = driver.find_element(by=By.XPATH, value=".//button[@type='submit']")
        sign_button.click()
        sleep(5)
        sign_button.click()
        self.log.info("The button has been pressed")

        sign_out = driver.find_element(by=By.XPATH, value=".//button[@class = 'btn btn-sm btn-secondary']")
        self.log.info("Button sign out was found")

        assert sign_out, f"Button Sign_Out not found {sign_out}"
