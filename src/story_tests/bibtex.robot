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
    Click Button  Add a New Reference
    Page Should Contain  Douglas Adams
    Click Element  //tr[td[text()='Douglas Adams']]
    Click Element  show-bibtex-button
    ${bibtex}=    Get Text    //pre[@id="bibtex-code"]
    Should Contain    ${bibtex}    @
    Should Contain    ${bibtex}    {
    Should Contain    ${bibtex}    title = {The Hitchhiker's Guide to the Galaxy}
    Should Contain    ${bibtex}    year = {1978}
    Should Contain    ${bibtex}    }

Ensure Reference Exists and Ensure BibTeX Format is Visible
    Go To  ${HOME_URL}

    ${book_title}  Set Variable  The Hitchhiker's Guide to the Galaxy
    ${book_author}  Set Variable  Douglas Adams
    ${book_year}  Set Variable  1978
    Create New Reference  book  ${book_title}  ${book_author}  ${book_year}  Harmony Books  9789510218440

    ${inproceeding_title}  Set Variable  Quantum Computing Conference
    ${inproceeding_author}  Set Variable  Richard Feynman
    ${inproceeding_year}  Set Variable  1981
    Create New Reference  inproceeding  ${inproceeding_title}  ${inproceeding_author}  ${inproceeding_year}  Proceedings of Quantum Computing  IEEE

    ${article_title}  Set Variable  Quantum Mechanics article
    ${article_author}  Set Variable  Albert Einstein
    ${article_year}  Set Variable  1925
    Create New Reference  article  ${article_title}  ${article_author}  ${article_year}  Annalen der Physik  3


    ${misc_title}  Set Variable  A Brief History of Time
    ${misc_author}  Set Variable  Stephen Hawking
    ${misc_year}  Set Variable  1988
    Create New Reference  misc  ${misc_title}  ${misc_author}  ${misc_year}  http://www.kemi.fi  visited 21.2.2021

    Click Element  show-bibtex-button
    ${bibtex}=    Get Text    //pre[@id="bibtex-code"]
    Should Contain    ${bibtex}    ${book_title}
    Should Contain    ${bibtex}    ${inproceeding_title}
    Should Contain    ${bibtex}    ${article_title}
    Should Contain    ${bibtex}    ${misc_title}

*** Keywords ***
Create New Reference
    [Arguments]  ${ref_type}  ${title}  ${author}  ${year}  ${arg1}  ${arg2}
    Click Link  Create a new reference
    Select From List By Value  ref_type  ${ref_type}
    Input Text  title  ${title}
    Input Text  author  ${author}
    Input Text  year  ${year}
    
    Run Keyword If  '${ref_type}' == 'book'  Input Text  publisher  ${arg1}
    Run Keyword If  '${ref_type}' == 'book'  Input Text  ISBN  ${arg2}

    Run Keyword If  '${ref_type}' == 'inproceeding'  Input Text  booktitle  ${arg1}
    Run Keyword If  '${ref_type}' == 'inproceeding'  Input Text  organization  ${arg2}

    Run Keyword If  '${ref_type}' == 'article'  Input Text  journal  ${arg1}
    Run Keyword If  '${ref_type}' == 'article'  Input Text  volume  ${arg2}

    Run Keyword If  '${ref_type}' == 'misc'  Input Text  url-misc  ${arg1}
    Run Keyword If  '${ref_type}' == 'misc'  Input Text  note  ${arg2}

    Click Button  Add a New Reference

    Page Should Contain  ${author}
