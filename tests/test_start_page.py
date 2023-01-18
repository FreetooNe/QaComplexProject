import logging
from time import sleep

from pages.hello_page import HelloPageConsts
from pages.start_page import StartPage
from pages.utils import random_str, random_num


class TestRegisterUser:
    """Tests for register form"""
    log = logging.getLogger("[Register form]")

    def test_registration(self, start_page):
        """
         -Description: Positive TEST: Registration new user
            - Steps:
                Fill username, Email, Password
                Click on button "Sign up for OurApp"
                Verify error
         """
        # Prepare test data
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{username_value}@gmail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Fill email, login and password fields
        hello_page = StartPage.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("User was registered ")

        # check for button Sign_Out
        hello_page.verify_sign_up_message(username_value)
        assert hello_page.verify_sign_up_message(username=username_value)
        self.log.info("Check for button Sign Out")

    def test_check_email_validation(self, start_page):
        """
         -Description: Checking for validation of the email field
            - Steps:
              Fill invalid email
              Verify error
         """

        # Fill incorrect email
        StartPage.sign_up(email='str123', password='', username='')
        self.log.info("Field were entered")
        sleep(1)
        # check for email validation massage
        assert StartPage.verify_sign_up
        self.log.info("Check email validation massage")

    def test_check_password_validation(self, start_page):
        """
        -Description: Checking for validation of the password field
             - Steps:
                Fill invalid password
                Verify error
        """

        # Fill incorrect password
        StartPage.sign_up(email='', password='123', username='')
        self.log.info("Filled incorrect password")

        # Check for password validation massage
        assert StartPage.verify_sign_up
        self.log.info("Check password validation massage")


class TestStartPage:
    """Tests for login form"""
    log = logging.getLogger("[Login_form]")

    def test_correct_data(self, start_page):
        """
         -Description: Positive TEST with correct Password and Login
             - Steps:
                  Fill  login and password
                  Click on SignIn button
                  Verify error
        """

        # login as valid user
        start_page.sign_in("Tverdokhlib", "Testtesttest")
        self.log.info("Login as correct user")
        sleep(2)
        # Verify button sign_out
        assert HelloPageConsts.SIGN_OUT_BUTTON_XPATH
        self.log.info("Verified button sign_out")

    def test_incorrect_password(self, start_page):
        """
        -Description: Negative TEST with incorrect Password and Login
           - Steps:
               Fill login and incorrect password
               Click on SignIn button
               Verify error
        """
        # login as incorrect login and password
        start_page.sign_in("Tverdokhlib", "incorrect_password")
        self.log.info("Login as incorrect password")
        sleep(1)
        # Verify Error massage
        assert StartPage.verify_sign_in
        self.log.info("Verify Error massage")

    def test_incorrect_login(self, start_page):
        """
        -Description: Negative TEST with incorrect Password and Login
            - Steps:
               Fill incorrect login and password
               Click on SignIn button
               Verify error
        """

        # login as invalid login
        start_page.sign_in("incorrect_login", "Testtesttest")
        self.log.info("Login as incorrect login")

        # Verify error
        assert start_page.verify_sign_in
        self.log.info("Error message was verified")
