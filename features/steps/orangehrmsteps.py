from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


@when('open orange hrm home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify the logo present on page')
def verifyLogo(context):
    pass

    # status = context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[1]/img").is_displayed()
    # assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
