*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***
Ensure Reference Exists and Ensure BibTeX Format is Visible
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  book
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  year  1978
    Input Text  publisher  Harmony Books
    Input Text  ISBN  9789510218440
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Element  //tr[td[text()='Douglas Adams']]
    Click Element  show-bibtex-button
    ${bibtex}=    Get Text    //pre[@id="bibtex-code"]
    Should Contain    ${bibtex}    @
    Should Contain    ${bibtex}    {
    Should Contain    ${bibtex}    title = {The Hitchhiker's Guide to the Galaxy}
    Should Contain    ${bibtex}    year = {1978}
    Should Contain    ${bibtex}    }