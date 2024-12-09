*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Create Book Reference With Tag
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  book
    Input Text  title  The Book of Tags
    Input Text  author  Mr. Graffiti
    Input Text  year  2005
    Input Text  publisher  Good Books
    Input Text  ISBN  7864738164889
    Input Text  tag_name  prio
    Click Button  Add a New Reference
    Wait Until Page Contains  Tag 'prio' added successfully

Add More Tags To an Existing Book Reference
    Go To  ${HOME_URL}
    Click Element  xpath://tr[td[text()='Mr. Graffiti']]
    Page Should Contain  prio
    Input Text  tag_name  essay
    Click Button  Add Tag
    Page Should Contain  essay
    Input Text  tag_name  read again
    Click Button  Add Tag
    Page Should Contain  read again
    Click Button  Save Changes
    Wait Until Page Contains  Reference updated successfully!

Delete Tag From Reference
    Go To  ${HOME_URL}
    Click Element  xpath://tr[td[text()='Mr. Graffiti']]
    Page Should Contain  prio
    Click Element  xpath://ul[@class='tag-list']/li[contains(., 'prio')]/form/button
    Page Should Not Contain  prio
    Page Should Contain  Tag deleted successfully

Add First Tag To an Existing Misc Reference
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  ref_type  misc
    Input Text  title  History of Computing
    Input Text  url-misc  https://example.com/history
    Click Button  Add a New Reference
    Page Should Contain  History of Computing
    Click Element  xpath://tr[td[text()='History of Computing']]
    Page Should Contain  No tags associated with this reference
    Input Text  tag_name  MVP
    Click Button  Add Tag
    Page Should Contain  MVP
    Click Button  Save Changes
