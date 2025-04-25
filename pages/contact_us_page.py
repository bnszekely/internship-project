from selenium.webdriver.common.by import By
from pages.base_page import Page

CONNECT_THE_COMPANY_BTN = (By.XPATH, "//*[text()='Connect the company']")

class ContactUsPage(Page):

    def verify_page_opens(self):
        self.verify_partial_url('contact-us')
        print("Current URL after click:", self.driver.current_url)

    def verify_connect_company_button_visible(self):
        self.wait_until_clickable(*CONNECT_THE_COMPANY_BTN)

