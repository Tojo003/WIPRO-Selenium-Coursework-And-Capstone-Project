*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://www.saucedemo.com/
${USERNAME}  standard_user
${PASSWORD}  secret_sauce

*** Test Cases ***
Login With Variables
    Open Browser    ${URL}    chrome
    Input Text    id=user-name    ${USERNAME}
    Input Password    id=password    ${PASSWORD}
    Click Button    id=login-button
    Page Should Contain    Products
    [Teardown]    Close All Browsers