import random
import time
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidCookieDomainException, TimeoutException, NoSuchElementException, \
    WebDriverException, ElementClickInterceptedException, StaleElementReferenceException


# from pageObjects import commonObjects
# from actions.HomeActions import HomeMethods


class GlobalActions(object):
    __TIMEOUT = 10

    def __init__(self, driver):
        super(GlobalActions, self).__init__()
        self._driver_wait = WebDriverWait(driver, GlobalActions.__TIMEOUT)
        self._driver = driver

    def open_page(self, url):
        self.driver.get(url)
        time.sleep(1)

    def scroll_into_view(self, duplet):
        element = GlobalActions.is_element_present(self, duplet)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', element)

    # Login method
    def wait_click(self, duplet):
        elem = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (duplet[0], duplet[1])))
        GlobalActions.scroll_into_view(self, duplet)
        time.sleep(1)
        elem.click()

    def find_click_retry(self, duplet, max_attempt=5):
        success = False
        attempt = 0
        while not success and attempt < max_attempt:
            try:
                element = GlobalActions.find_element_duplet(self, duplet)
                element.click()
                success = True
                return element
            except (WebDriverException, StaleElementReferenceException, NoSuchElementException,
                    ElementClickInterceptedException) as e:
                print('single click attempt failed, retrying.... Exception: ' + str(e))
                time.sleep(0.5)
                attempt += 1
        assert success, "The element couldn't be clicked!"

    def find_element_duplet(self, duplet):
        return self.driver.find_element(duplet[0], duplet[1])

    def send_keys(self, duplet, key):
        elem = GlobalActions.find_element_duplet(self, duplet)
        elem.send_keys(key)

    def fill_input_box(self, duplet, text):
        GlobalActions.is_element_present(self, duplet)
        GlobalActions.send_keys(self, duplet, text)

    def generate_random_number(self, min, max):
        value = random.randint(min, max)
        return value

    def is_element_present(self, duplet):
        try:

            elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((duplet[0], duplet[1])))
            print("elem found")

        except NoSuchElementException:
            print("elem not found")
            return False
        return elem

    def clear_input_box(self, duplet):
        elem = GlobalActions.find_element_duplet(self, duplet)
        elem.clear()

    def is_element_present_bool(self, how, what):
        try:

            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((how, what)))

        except:
            pass
            return False
        return True