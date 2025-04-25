from selenium.webdriver.common.by import By
from pages.base_page import Page

CONTACT_US_BTTN = (By.XPATH, "//div[contains(text(),'Contact us')]")


class SettingsPage(Page):
    def click_contact_us_btn(self):
        self.click(*CONTACT_US_BTTN)

