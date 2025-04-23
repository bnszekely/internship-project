from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@when('Click on Contact us option')
def click_on_contact_us_btn(context):
    context.app.settings_page.click_contact_us_btn()
