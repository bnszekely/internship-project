from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SOCIAL_MEDIA_ICONS = (By.XPATH, "//div[@class='social-button']")


@then('Verify the right page opens')
def verify_page_opens(context):
    context.app.contact_us_page.verify_page_opens()


@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    social_media_icons = context.driver.find_elements(*SOCIAL_MEDIA_ICONS)
    assert len(social_media_icons) >= 4, f'Error. Expected at least 4 icons, got {len(social_media_icons)}'


@then('Verify the Connect the company button is available and clickable')
def verify_connect_company_button_visible(context):
    context.app.contact_us_page.verify_connect_company_button_visible()
