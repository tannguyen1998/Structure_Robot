*** Settings ***
Resource  Common_Locator.robot

*** Keywords ***
Get Title On Page
    [Arguments]  ${txt_title}
    ${title_page}   verify title on page
    should be equal  ${title_page}  ${txt_title}

Click Element On Page
    Click Element   ${btn_search}

Input Value On Page
    [Arguments]  ${text_destination}
    Wait Element Is Visible     ${txt_google}
    Input Value     ${txt_google}    ${text_destination}