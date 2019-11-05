*** Settings ***
Resource  ../Common/Common.robot
Resource  Google_Locator.robot

*** Keywords ***
Verify Title On Page
    Verify Title Page

Input Text On Page
    [Arguments]  ${txt_google}
    Input Text Element  ${element_input}    ${txt_google}