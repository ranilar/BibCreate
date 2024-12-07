*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***

#Book tests:
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
    Page Should Not Contain  Douglas Adams

Editing book reference works
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
    Click Element  xpath://tr[td[text()='Douglas Adams']]
    Input Text  title  The Hitchhiker's Guide to the Editing
    Input Text  author  Douglas Editor
    Input Text  year  1979
    Input Text  publisher  Harmony Edits
    Input Text  ISBN  9789510218441
    Click Button    Save Changes
    Page Should Contain  Douglas Editor

#Article tests:
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
    Click Button  X
    Page Should Not Contain   Douglas Adam

Editing article reference works
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  article
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  journal  Intergalactic Science Journal
    Input Text  year  1978
    Input Text  volume  42
    Input Text  DOI-article  10.1000/182
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Element  xpath://tr[td[text()='Douglas Adams']]
    Input Text  title  The Hitchhiker's Guide to the Editing
    Input Text  author  Douglas Editor
    Input Text  journal  Intergalactic Science Editing
    Input Text  year  1979
    Input Text  volume  43
    Click Button    Save Changes
    Page Should Contain  Douglas Editor

#Misc tests
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
    Click Button  X
    Page Should Not Contain   Dougla Adams

Editing misc reference works
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  misc
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  year  1978
    Input Text  url-misc  https://example.com/hitchhikers-guide
    Input Text  note  Classic sci-fi book reference
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Element  xpath://tr[td[text()='Douglas Adams']]
    Input Text  title  The Hitchhiker's Guide to the Editing
    Input Text  author  Douglas Editor
    Input Text  year  1979
    Input Text  note  Classic sci-fi book edit
    Click Button    Save Changes
    Page Should Contain  Douglas Editor

#inproceedings tests
After deleting a inproceeding reference, site doesnt display it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  inproceeding
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  year  1978
    Input Text  booktitle  Proceedings of the Galactic Conference
    Input Text  DOI-inproceeding  10.1000/182
    Input Text  address  Magrathea 12
    Input Text  month  October
    Input Text  url-inproceeding  https://example.com/galactic-conference
    Input Text  organization  Galactic Publishing
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Button  X
    Page Should Not Contain   Douglas Adams

Editing inproceeding works
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  inproceeding
    Input Text  title  The Hitchhiker's Guide to the Galaxy
    Input Text  author  Douglas Adams
    Input Text  year  1978
    Input Text  booktitle  Proceedings of the Galactic Conference
    Input Text  DOI-inproceeding  10.1000/182
    Input Text  address  Magrathea 12
    Input Text  month  October
    Input Text  url-inproceeding  https://example.com/galactic-conference
    Input Text  organization  Galactic Publishing
    Click Button  Add
    Page Should Contain  Douglas Adams
    Click Element  xpath://tr[td[text()='Douglas Adams']]
    Input Text  title  The Hitchhiker's Guide to the Editing
    Input Text  author  Douglas Editor
    Input Text  year  1979
    Input Text  booktitle  Proceedings of the Galactic Editing
    Input Text  month  December
    Input Text  organization  Galactic Editing
    Click Button    Save Changes
    Page Should Contain  Douglas Editor

#Ref search tests
Searching for a reference
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
    Click Link  Create a new reference
    Select From List By Value  ref_type  article
    Input Text  title  The Biker's Guide to the Galaxy
    Input Text  author  Douglas Adam
    Input Text  journal  Intergalactic Science Journal
    Input Text  year  1978
    Input Text  volume  42
    Input Text  DOI-article  10.1000/182
    Click Button  Add
    Page Should Contain  Douglas Adam
    Input Text  query  The Hitch
    Click Button  Search
    Page Should Contain  The Hitchhiker's Guide to the Galaxy
    Page Should Not Contain  The Biker's Guide to the Galaxy
    Click Element  xpath://tr[td[text()='Douglas Adam']]
    Input Text  title  The Hitchhiker's Guide to the Editing
    Input Text  author  Douglas Editor
    Input Text  year  1979
    Click Button    Save Changes
    Page Should Contain  Douglas Editor

Searching with tag
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
    Input Text  tag_name  readinglist
    Click Button  Add
    Page Should Contain  Douglas Adam
    Click Link  Create a new reference
    Select From List By Value  ref_type  article
    Input Text  title  The Biker's Guide to the Galaxy
    Input Text  author  Douglas Biker
    Input Text  journal  Intergalactic Science Journal
    Input Text  year  1978
    Input Text  volume  42
    Input Text  DOI-article  10.1000/182
    Input Text  tag_name  done reading
    Click Button  Add
    Page Should Contain  Douglas Biker
    Input Text  query  done reading
    Click Button  Search
    Page Should Contain  The Biker's Guide to the Galaxy
    Page Should Not Contain  The hitchhiker's Guide to the Galaxy
