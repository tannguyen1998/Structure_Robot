*** Settings ***
Documentation  Check Result On Page
Resource   ../../Resources/Pages/Google_Pages.robot
Variables  ../../Data/Google.yaml

Suite Setup      Open Browser On Page   ${1_1.url}  ${1_1.driver}
Suite Teardown   Clean Up Data
Force Tags   Google_Management 1_1

*** Test Cases ***
Test Case 01: Check Title On Page
    [Documentation]  Test Result About Title
    [Tags]  1_1_2
    Given User Verify Title On Page
    When User Input Text On Page Google     ${1_1.text_google}
