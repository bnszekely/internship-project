from selenium.webdriver.common.by import By
from pages.base_page import Page


LOG_IN_BTN = (By.XPATH, "//div[contains(text(),'Log in')]")
SETTINGS_ICON = (By.XPATH, "//div[@class='settings-code w-embed']")

class MainPage(Page):

    def open_main_page(self):
        self.open_url(self.base_url)

    def click_settings_icon(self):
        self.wait_until_clickable(*SETTINGS_ICON)
        self.find_element(*SETTINGS_ICON).click()

