*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***

After adding a book reference, site displays it
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

After deleting a book reference, site doesnt display it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  book
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adas
    Input Text  year  1978
    Input Text  publisher  Harmony Books
    Input Text  ISBN  9789510218440
    Page Should Not Contain  Douglas Adas


After deleting a article reference, site doesnt display it
    Reset References
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  article
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adam
    Input Text  journal  Intergalactic Science Journal
    Input Text  year  1978
    Input Text  volume  42
    Input Text  DOI-article  10.1000/182
    Click Button  Add
    Page Should Contain  Douglas Adam
    Click Button  x
    Page Should Not Contain   Douglas Adam

After deleting a misc reference, site doesnt display it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  misc
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Dougla Adams
    Input Text  year  1978
    Input Text  url-misc  https://example.com/hitchhikers-guide
    Input Text  note  Classic sci-fi book reference
    Click Button  Add
    Page Should Contain  Dougla Adams
    Click Button  x
    Page Should Not Contain   Dougla Adams

After deleting a inproceeding reference, site doesnt display it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  inproceeding
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Ad
    Input Text  year  1978
    Input Text  booktitle  Proceedings of the Galactic Conference
    Input Text  DOI-inproceeding  10.1000/182
    Input Text  address  Magrathea 12
    Input Text  month  October
    Input Text  url-inproceeding  https://example.com/galactic-conference
    Input Text  organization  Galactic Publishing
    Click Button  Add
    Page Should Contain  Douglas Ad
    Click Button  x
    Page Should Not Contain   Douglas Ad

*** Keywords ***