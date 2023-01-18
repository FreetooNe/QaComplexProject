class StartPageConst:
    """Stores constants related to start page"""
    # Sign In
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT = 'Sing In'
    SIGN_IN_BUTTON_XPATH = f".//button[text()='{SIGN_IN_BUTTON_TEXT}']"
    SIGN_IN_ERROR_TEXT = 'Error'
    SIGN_IN_ERROR_XPATH = f".//button[@class = 'btn btn-sm btn-secondary']"

    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id = 'username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id = 'email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id = 'password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    SIGN_UP_VALIDATION_EMAIL_TEXT = "You must provide a valid email address."
    SIGN_UP_VALIDATION_EMAIL_XPATH = ".//input[@id = 'email-register']"
    SIGN_UP_VALIDATION_PASSWORD_TEXT = "Password must be at least 12 characters."
    SIGN_UP_VALIDATION_PASSWORD_XPATH = ".//input[@id = 'password-register']"