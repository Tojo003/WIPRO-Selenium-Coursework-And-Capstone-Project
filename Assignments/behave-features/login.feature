Feature: SauceDemo login

  Scenario: Valid login
    Given SauceDemo is open
    When I login with "standard_user" and "secret_sauce"
    Then the inventory page is displayed
