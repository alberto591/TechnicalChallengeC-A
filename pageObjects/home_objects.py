from selenium.webdriver.common.by import By

cookies_btn = [By.XPATH, "//button[@id='onetrust-accept-btn-handler']"]
register_btn = [By.XPATH, "//a[@href='/es/es/shop/account/register']"]
header_account_btn = [By.XPATH, "//button[@data-qa='HeaderAccountButton']"]
continue_register_btn = [By.XPATH, "//section[@data-qa='MembershipTeaser']//div//div//button"]
email_address_input = [By.ID, "emailAddress"]
loading_btn = [By.XPATH, "//button[@data-qa='LoadingButton']"]
first_name_input = [By.ID, "firstName"]
last_name_input = [By.ID, "lastName"]
password_input = [By.ID, "password"]
checkbox_reg_input = [By.XPATH, "//label[@data-qa='Checkbox']//div"]
login_email_input = [By.ID, "myaccount_login_email"]
login_password_input = [By.ID, "myaccount_login_password"]
headline_text = [By.XPATH, "//div[@data-qa='Headline']"]
notification_text = [By.XPATH, "//div[@data-qa='Notification']"]
empty_orders = [By.XPATH, "//section[@data-qa='EmptyOrders']"]
close_btn_error = [By.XPATH, "//button[@Title='Todo listo']"]
error_message_login = [By.XPATH, "//div[@data-qa='Copy']"]


