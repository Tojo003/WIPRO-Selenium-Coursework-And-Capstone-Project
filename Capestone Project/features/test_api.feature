Feature: Automated REST API Testing Suite

  Scenario: GET - Retrieve Products List
    Given the target endpoint URL is "https://automationexercise.com/api/productsList"
    When I send a "GET" request
    Then the HTTP status code should be 200
    And the JSON responseCode should be 200

  Scenario: POST - Search Product with Missing Parameter
    Given the target endpoint URL is "https://automationexercise.com/api/searchProduct"
    When I send a "POST" request
    Then the HTTP status code should be 200
    And the JSON responseCode should be 400
    And the response body message should be "Bad request, search_product parameter is missing in POST request."

  Scenario: PUT - Update Account for Non-Existent User
    Given the target endpoint URL is "https://automationexercise.com/api/updateAccount"
    And request payload parameter "name" is set to "Test User"
    And request payload parameter "email" is set to "invalid_user_99999@example.com"
    And request payload parameter "password" is set to "invalid_pass"
    And request payload parameter "title" is set to "Mr"
    And request payload parameter "birth_date" is set to "15"
    And request payload parameter "birth_month" is set to "08"
    And request payload parameter "birth_year" is set to "1990"
    And request payload parameter "firstname" is set to "Test"
    And request payload parameter "lastname" is set to "User"
    And request payload parameter "company" is set to "Automation Corp"
    And request payload parameter "address1" is set to "404 Not Found Street"
    And request payload parameter "address2" is set to "Suite 000"
    And request payload parameter "country" is set to "India"
    And request payload parameter "zipcode" is set to "700001"
    And request payload parameter "state" is set to "West Bengal"
    And request payload parameter "city" is set to "Kolkata"
    And request payload parameter "mobile_number" is set to "9999999999"
    When I send a "PUT" request with payload
    Then the HTTP status code should be 200
    And the JSON responseCode should be 404
    And the response body message should be "Account not found!"

  Scenario: DELETE - Delete Account with Non-Existent User
    Given the target endpoint URL is "https://automationexercise.com/api/deleteAccount"
    And request payload parameter "email" is set to "invalid_user_99999@example.com"
    And request payload parameter "password" is set to "invalid_pass"
    When I send a "DELETE" request with payload
    Then the HTTP status code should be 200
    And the JSON responseCode should be 404
    And the response body message should be "Account not found!"

  Scenario: DELETE - Delete Valid Account
    Given the target endpoint URL is "https://automationexercise.com/api/deleteAccount"
    And request payload parameter "email" is set to "invalid_user_99999@example.com"
    And request payload parameter "password" is set to "invalid_pass"
    When I send a "DELETE" request with payload
    Then the HTTP status code should be 200
    And the JSON responseCode should be 404
    And the response body message should be "Account not found!"