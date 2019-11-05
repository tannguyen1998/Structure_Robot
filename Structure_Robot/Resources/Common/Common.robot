*** Settings ***
Documentation  Keywords common
Library   ICOLibrary
Resource  Common_Actions.robot

*** Keywords ***
Open Browser On Page
    [Arguments]   ${url}    ${driver}
    open browser  ${url}   ${driver}
    maximize browser window

Clean Up Data
    close browser