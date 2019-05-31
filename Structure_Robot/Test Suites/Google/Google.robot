*** Settings ***
Documentation  Check Result On Page
Resource   ../../Pages/google_pages.robot
Variables  ../../Resource/Data/Google.yaml

Suite Setup      Open Browser On Page
Suite Teardown   Clean Up Data
Force Tags   Google_Management 1_1

*** Test Cases ***
Test Case 01: Check Title On Page
    [Documentation]  Test Result About Title
    [Tags]  1_1_2
    User Verify Title On Page

