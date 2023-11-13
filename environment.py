import re
import time
import allure
from behave import fixture, use_fixture
import pytz
from selenium import webdriver
from datetime import datetime



@fixture
def browser_chrome(context, feature):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome()
    context.browser = context.driver
    time.sleep(3)
    print("context.driver:", context.driver)
    context.driver.maximize_window()
    yield context.driver
    context.driver.quit()


def before_all(context):
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Starting at {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("---------------------------------------------------------------------------------------------------------")
    context.test_start_time = datetime.now(pytz.utc)


def before_feature(context, feature):
    feature_name = re.search('\"(.*)\"', str(feature)).group(1)
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Before feature: {feature_name}")
    print(f"Starting at {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("---------------------------------------------------------------------------------------------------------")
    print(" ")
    context.feature_start_time = datetime.now(pytz.utc)
    print("context", context)
    use_fixture(browser_chrome, context, feature)


def before_scenario(context, scenario):
    scenario_name = re.search('\"(.*)\"', str(scenario)).group(1)
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Before scenario: {scenario_name}")
    print(f"Starting at {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("---------------------------------------------------------------------------------------------------------")
    print(" ")
    context.scenario_start_time = datetime.now(pytz.utc)
    context.driver.delete_all_cookies()



def before_step(context, step):
    step_name = re.search('\"(.*)\"', str(step)).group(1)
    print(f"Step name: {step_name}")


def after_step(context, step):
    step_name = re.search('\"(.*)\"', str(step)).group(1)


def after_scenario(context, scenario):
    print('after_scenario')
    scenario_start_time = context.scenario_start_time
    scenario_end_time = datetime.now(pytz.utc)
    scenario_load_time = (scenario_end_time - scenario_start_time).total_seconds()
    scenario_minutes = (scenario_load_time / 60)
    print("---------------------------------------------------------------------------------------------------------")
    print(f"{scenario}")
    print(f"Scenario finished at {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print(f"Total time to complete = {round(scenario_load_time, 2)} seconds ({round(scenario_minutes, 2)} minutes) ")
    print("---------------------------------------------------------------------------------------------------------")
    print(" ")
    context.driver.delete_all_cookies()

    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot_after_failure',
                      attachment_type=allure.attachment_type.PNG)
    elif scenario.status == "passed":
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot_after_passing',
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    start_time = context.test_start_time
    end_time = datetime.now(pytz.utc)
    total_load_time = (end_time - start_time).total_seconds()
    all_minutes = (total_load_time / 60)
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Test finished at {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print(f"Total time to complete = {round(total_load_time, 2)} seconds ({round(all_minutes, 2)} minutes) ")
    print("---------------------------------------------------------------------------------------------------------")
    print(" ")
