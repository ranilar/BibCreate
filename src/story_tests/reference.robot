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
    Input Text  author  Douglas Adams
    Input Text  year  1978
    Input Text  publisher  Harmony Books
    Input Text  ISBN  9789510218440
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Button  x
    Page Should Not Contain   Douglas Adams

After deleting a article reference, site doesnt display it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  article
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  journal  Intergalactic Science Journal
    Input Text  year  1978
    Input Text  volume  42
    Input Text  DOI  10.1000/182
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Button  x
    Page Should Not Contain   Douglas Adams

After deleting a misc reference, site doesnt display it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  misc
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  year  1978
    Input Text  url  https://example.com/hitchhikers-guide
    Input Text  note  Classic sci-fi book reference
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Button  x
    Page Should Not Contain   Douglas Adams

After deleting a inproceedings reference, site doesnt display it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  inproceedings
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  year  1978
    Input Text  booktitle  Proceedings of the Galactic Conference
    Input Text  DOI  10.1000/182 #Tässä tulee error, ei tule esim. article DOI kohdassa?
    Input Text  address  Magrathea 12
    Input Text  month  October
    Input Text  url  https://example.com/galactic-conference
    Input Text  organization  Galactic Publishing
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Button  x
    Page Should Not Contain   Douglas Adams

*** Keywords ***