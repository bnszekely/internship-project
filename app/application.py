from pages.base_page import Page
from pages.contact_us_page import ContactUsPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)
