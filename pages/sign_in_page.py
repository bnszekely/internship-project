from selenium.webdriver.common.by import By
from pages.base_page import Page

EMAIL_FIELD = (By.CSS_SELECTOR, '#email-2')
PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
LOGIN_BUTTON = (By.XPATH,"//a[@class='login-button w-button']")

class SignInPage(Page):

    def enter_email(self, email):
        self.wait_until_visible(*EMAIL_FIELD)
        self.input_text(email, *EMAIL_FIELD)

    def enter_password(self, password):
        self.input_text(password, *PASSWORD_FIELD)

    def click_login(self):
        self.click(*LOGIN_BUTTON)

    def sign_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()