import logging
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_start_page(self):
        """
                    -Description: Positive TEST with correct Password and Login
                       - Pre-conditions:
                           1 - Open start page
                       - Steps:
                           2 - Fill login
                           3 - Fill password
                           4 - Click on SignIn button
                           5 - Verify error
                       """
        # Open start page
        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # fill login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("Tverdokhlib")
        self.log.info("filled login")
        sleep(1)

        # fill password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys("Testtesttest")
        self.log.info("filled password]")
        sleep(1)

        # click on button signIn
        signin_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        signin_button.click()
        self.log.info("click button sign in")
        sleep(1)

        # find for a button SignIn
        sign_out = driver.find_element(by=By.XPATH, value=".//button[@class = 'btn btn-sm btn-secondary']")
        self.log.info("Button sign out was found")

        # checking for an error message
        assert sign_out, f"Button Sign_Out not found {sign_out}"

        driver.close()

        """
            -Description: Negative TEST with incorrect Password and Login
               - Pre-conditions:
                   1 - Open start page
               - Steps:
                   2 - Fill login
                   3 - Fill password
                   4 - Click on SignIn button
                   5 - Verify error
               """
        # Open start page
        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # fill incorrect login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys(f"email{randint(1, 200)}.com")
        self.log.info("filled loggin")
        sleep(1)

        # fill incorrect password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys(f"{randint(1000, 2000)}")
        self.log.info("filled password]")
        sleep(1)

        # click on button signIn
        signin_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        signin_button.click()
        self.log.info("click button sign in")
        sleep(1)

        # find for a button SignIn
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        self.log.info("Error message was verified")

        # checking for an error message
        assert error_message.text == 'Error'

        driver.close()

        """
               -Description: Negative TEST with correct Password and incorrect Login
                  - Pre-conditions:
                      1 - Open start page
                  - Steps:
                      2 - Fill incorrect login
                      3 - Fill correct password
                      4 - Click on SignIn button
                      5 - Verify error
                  """

        # Open start page

        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill incorrect login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("IncorrectLogin")
        self.log.info("filled login")
        sleep(1)

        # Fill correct password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys("Testtesttest")
        self.log.info("filled password]")
        sleep(1)

        # click on button signIn
        signin_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        signin_button.click()
        self.log.info("click button sign in")
        sleep(1)

        # find error message
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        self.log.info("Error message was verified")

        # checking for an error message
        assert error_message.text == 'Error'

        # end test
        driver.close()

        """
                      -Description: Negative TEST with incorrect Password and correct Login
                         - Pre-conditions:
                             1 - Open start page
                         - Steps:
                             2 - Fill incorrect login
                             3 - Fill correct password
                             4 - Click on SignIn button
                             5 - Verify error
                         """

        driver = webdriver.Chrome(executable_path="/Users/ablofon8/PycharmProjects/QaComplex/chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill correct login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("Tverdokhlib")
        self.log.info("filled login")
        sleep(1)

        # Fill incorrect password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys("1233213123")
        self.log.info("filled password]")
        sleep(1)

        # click on button signIn
        signin_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        signin_button.click()
        self.log.info("click button sign in")
        sleep(1)

        # Find  error massage
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        self.log.info("Error message was verified")

        # checking for an error message
        assert error_message.text == 'Error'

        driver.close()
