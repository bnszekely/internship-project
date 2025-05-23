from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options
from support.logger import logger


#Command to run tests with Allure & Behave:
#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/reelly_contact.feature


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """


    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "Nexus 5"})

    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    ### SAFARI ###
    #context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
         #options=options,
        # service=service
     #)

    ### BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #bs_user = 'brittanyszekely_0KARD6'
    #bs_key = 'MpB3xunpt9V3bSqsjG7A'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = Options()
    #bstack_options = {
    #"os": "Windows",
    #'browserName': 'edge',
    #'sessionName': scenario_name,
     #}
    #options.set_capability('bstack:options', bstack_options)
    #context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)


    context.app = Application(context.driver)
    from pages.sign_in_page import SignInPage
    context.sign_in_page = SignInPage(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
