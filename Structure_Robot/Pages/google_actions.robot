*** Settings ***
Library   ICOLibrary
Resource  ../Common/Common.robot
Variables  google_locator.robot

*** Keywords ***
Verify Title On Page
    verify title page