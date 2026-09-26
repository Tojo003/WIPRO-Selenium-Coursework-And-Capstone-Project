*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Setup And Teardown
    [Setup]    Open Browser    https://www.saucedemo.com/    chrome
    Title Should Be    Swag Labs
    [Teardown]    Close All Browsers*** Test Cases ***
