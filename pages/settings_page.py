from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CONTACT_US_BTTN = (By.XPATH, "//div[contains(text(),'Contact us')]")


class SettingsPage(Page):

    def click_contact_us_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CONTACT_US_BTTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CONTACT_US_BTTN)
        ).click()
