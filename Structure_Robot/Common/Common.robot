*** Settings ***
Documentation  Keywords common
Resource  Common_Actions.robot

*** Keywords ***
Open Browser On Page
    open browser  ${URL}    chrome

Clean Up Data
    close browser