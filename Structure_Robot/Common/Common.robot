*** Settings ***
Documentation  Keywords common
Library   ICOLibrary
Resource  Common_Actions.robot

*** Keywords ***
Open Browser On Page
    open browser  ${URL}    chrome
    maximize browser window

Clean Up Data
    close browser