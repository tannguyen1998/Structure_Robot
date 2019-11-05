*** Settings ***
Resource  Google_Actions.robot

*** Keywords ***
User Verify Title On Page
    Verify Title On Page

User Input Text On Page Google
    [Arguments]  ${txt_google}
    Input Text On Page  ${txt_google}