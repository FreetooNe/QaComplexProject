import logging
from time import sleep

from constants.hello_page import HelloPageConsts
from constants.start_page import StartPageConst
from pages.base_page import BasePage


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.consthellopage = HelloPageConsts
        self.log = logging.getLogger("[TestStartPage]")

    def sign_in(self, username, password):
        """Sign in using provided values"""

        # fill fields
        self.fill_field(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        sleep(1)

        # click on button signIn
        self.click(self.const.SIGN_IN_BUTTON_XPATH)
        sleep(1)

    def verify_sign_in(self):
        """Verify that text is matches tp expected"""

        self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_XPATH, text=self.const.SIGN_IN_ERROR_TEXT)

    def sign_up(self, username, email, password):
        """sign up using provided values"""
        # fill fields
        self.fill_field(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        sleep(2)

        # click on button signIn
        self.click(self.const.SIGN_UP_BUTTON_XPATH)
        sleep(2)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    def verify_sign_up(self):
        """Verify that text is matches tp expected"""
        self.compare_element_text(xpath=self.const.SIGN_UP_VALIDATION_EMAIL_XPATH,
                                  text=self.const.SIGN_UP_VALIDATION_EMAIL_TEXT)

        self.compare_element_text(xpath=self.const.SIGN_UP_VALIDATION_PASSWORD_XPATH,
                                  text=self.const.SIGN_UP_VALIDATION_PASSWORD_TEXT)
