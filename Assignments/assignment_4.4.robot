*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open SauceDemo
    Open Browser    https://www.saucedemo.com/    firefox

*** Test Cases ***
Custom Keyword Test
    Open SauceDemo
    Title Should Be    Swag Labs
    [Teardown]    Close All Browsers