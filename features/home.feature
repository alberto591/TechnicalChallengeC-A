Feature:  User register and login

Background: Access home page
  Given a user access to the home page

  @validation
  Scenario: Validation field is applied in the registration form and login user field
    Given a user selects to register a new user
    When user does not fill in the register form correctly and validations are applied
    Then the user is not created

  @register
  Scenario: User register
    Given a user selects to register a new user
    When user fill in the register form
    Then the user is created

   @login
  Scenario Outline: Error message is shown when adding incorrect data for login functionality
    Given a registered user attempts to log in from the home page
    When fill in "<username>" and "<password>" in the log in fields
    Then error message is shown to the user
    Examples:
    | username              | password          |
    | testUser32@gmail.com  | wrongpasswordd    |
    | emailnoexist@test.com | Password1!        |

  @login
  Scenario Outline: Registered user is logging in
    Given a registered user attempts to log in from the home page
    When fill in "<username>" and "<password>" in the log in fields
    Then user successfully logs in to the account
    Examples:
    | username              | password       |
    | testUser32@gmail.com  | Password1!     |