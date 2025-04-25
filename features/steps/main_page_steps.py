from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Click on the settings icon')
def click_settings_icon(context):
    context.app.main_page.click_settings_icon()
    sleep(1)