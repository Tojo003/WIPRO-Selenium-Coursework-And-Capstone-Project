*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Tagged Test
    [Tags]    smoke
    Open Browser    https://www.saucedemo.com/    chrome
    Title Should Be    Swag Labs
    [Teardown]    Close All Browsers