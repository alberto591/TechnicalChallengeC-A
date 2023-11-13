from behave import *
from actions.home_actions import HomeActions


@step('a user access to the home page')
def access_home_pager(context):
    HomeActions.access_home_page(context)


@step('a user selects to register a new user')
def register_user(context):
    HomeActions.register_user(context)


@step('user fill in the register form')
def fill_in_submit_register_form(context):
    HomeActions.fill_in_submit_register_form(context)


@step('the user is created')
def user_created_verified(context):
    HomeActions.user_created_verified(context)


@step('a registered user attempts to log in from the home page')
def select_login_btn(context):
    HomeActions.select_login_btn(context)


@step('fill in "{username}" and "{password}" in the log in fields')
def fill_in_login_data(context, username, password):
    HomeActions.fill_in_login_data(context, username, password)


@step('user successfully logs in to the account')
def user_logged_in(context):
    HomeActions.user_logged_in(context)


@step('user does not fill in the register form correctly and validations are applied')
def register_form_validations(context):
    HomeActions.register_form_validations(context)


@step('the user is not created')
def user_is_not_logged_in(context):
    HomeActions.user_is_not_logged_in(context)

@step('error message is shown to the user')
def error_message_shown(context):
    HomeActions.error_message_shown(context)