import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open orange HRM home page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    time.sleep(2)
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)


@when('click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()


@then('user must successfully login to the dashboard page')
def step_impl(context):
    time.sleep(3)
    try:
        text = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
