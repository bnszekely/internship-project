from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@Given('Log in to the page with email "{email}" and password "{password}"')
def log_in_to_the_page(context, email, password):
    context.sign_in_page.open_url(context.sign_in_page.base_url)
    context.sign_in_page.sign_in(email, password)
