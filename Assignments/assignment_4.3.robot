*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verify Element
    Open Browser    https://www.saucedemo.com/    chrome
    Page Should Contain Element    id=user-name
    [Teardown]    Close All Browsers