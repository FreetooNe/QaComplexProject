import logging
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    """
           - Pre-conditions:
               1 - Open start page
           - Steps:
               2 - Fill login
               3 - Fill password
               4 - Click on SignIn button
               5 - Verify error
           """

    # step 1
    def test_start_page(self):
        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # fill login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys(f"email{randint(1, 200)}.com")
        self.log.info("filled loggin")
        sleep(1)

        # fill password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys(f"{randint(1000, 2000)}")
        self.log.info("filled password]")
        sleep(1)

        signin_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        signin_button.click()
        self.log.info("click button sign in")
        sleep(1)

        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == 'Error'
        self.log.info("Error message was verified")

        driver.close()

    class Registred_new_user:
        log = logging.getLogger("[StartPage]")
