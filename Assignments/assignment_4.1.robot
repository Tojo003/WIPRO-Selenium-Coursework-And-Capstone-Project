*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Browser
    Open Browser    https://www.saucedemo.com/    chrome
    Title Should Be    Swag Labs
    [Teardown]    Close All Browsers