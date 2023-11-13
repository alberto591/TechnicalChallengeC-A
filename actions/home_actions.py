import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from actions.global_actions import GlobalActions
from pageObjects import home_objects


class HomeActions(object):
    __TIMEOUT = 10

    def __init__(self, driver):
        super(GlobalActions, self).__init__()
        self._driver_wait = WebDriverWait(driver, GlobalActions.__TIMEOUT)
        self._driver = driver


    def access_home_page(self):
        GlobalActions.open_page(self, "https://www.c-and-a.com/es/es/shop")
        GlobalActions.wait_click(self, home_objects.cookies_btn)


    def register_user(self):
        randomNumber = GlobalActions.generate_random_number(self, 1, 10000)
        email = "testUser" + str(randomNumber) + "@gmail.com"
        time.sleep(1)
        GlobalActions.wait_click(self, home_objects.register_btn)
        GlobalActions.fill_input_box(self, home_objects.email_address_input, email)
        GlobalActions.wait_click(self, home_objects.loading_btn)

    def fill_in_submit_register_form(self):
        GlobalActions.fill_input_box(self, home_objects.first_name_input, "testName")
        GlobalActions.fill_input_box(self, home_objects.last_name_input, "testLastName")
        GlobalActions.fill_input_box(self, home_objects.password_input, "Password1!")
        GlobalActions.wait_click(self, home_objects.checkbox_reg_input)
        GlobalActions.wait_click(self, home_objects.loading_btn)

    def user_created_verified(self):
        GlobalActions.is_element_present(self, home_objects.headline_text)

    def select_login_btn(self):
        GlobalActions.wait_click(self, home_objects.header_account_btn)

    def fill_in_login_data(self, username, password):
        GlobalActions.fill_input_box(self, home_objects.login_email_input, username)
        GlobalActions.fill_input_box(self, home_objects.login_password_input, password)
        GlobalActions.wait_click(self, home_objects.loading_btn)

    def user_logged_in(self):
        GlobalActions.wait_click(self, home_objects.header_account_btn)
        GlobalActions.is_element_present(self, home_objects.headline_text)

    def register_form_validations(self):
        GlobalActions.fill_input_box(self, home_objects.first_name_input, "testName")
        GlobalActions.fill_input_box(self, home_objects.last_name_input, "testLastName")
        # validating form with wrong input for password field
        GlobalActions.fill_input_box(self, home_objects.password_input, "!")
        GlobalActions.wait_click(self, home_objects.loading_btn)
        time.sleep(1)
        GlobalActions.find_element_duplet(self, home_objects.notification_text)
        # validating form with no input for password field
        GlobalActions.clear_input_box(self, home_objects.password_input)
        GlobalActions.wait_click(self, home_objects.loading_btn)
        time.sleep(1)
        # validating form missing number for password field
        GlobalActions.fill_input_box(self, home_objects.password_input, "Password!")
        GlobalActions.wait_click(self, home_objects.loading_btn)
        time.sleep(1)
        GlobalActions.wait_click(self, home_objects.close_btn_error)

    def user_is_not_logged_in(self):
        bool = GlobalActions.is_element_present_bool(self, By.XPATH, "//section[@data-qa='EmptyOrders']")
        assert bool == False, "User account is created but it should not be created"

    def error_message_shown(self):
        GlobalActions.is_element_present(self, home_objects.error_message_login)
