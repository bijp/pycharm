*** Settings ***
Library   SeleniumLibrary
Library   Collections
Library   deleteAllCourse

*** Keywords ***
loginwebsite
    [Arguments]     ${username}       ${password}
    open browser    http://localhost/mgr/login/login.html   chrome
    set browser implicit wait  10
    input text      id=username         ${username}
    input text      id=password         ${password}
    click element   css=.btn-success
addcourse
    [Arguments]         ${coursename}     ${coursedesc}    ${courseidx}
    click element   css=[ng-click="showAddOne=true"]
    input text      css=[ng-model="addData.name"]    ${coursename}
    input text      css=[ng-model="addData.desc"]    ${coursedesc}
    input text      css=[ng-model="addData.display_idx"]    ${courseidx}
    click element    css=[ng-click="addOne()"]
    sleep   3
GetCourseList
    ${eles}    Get WebElements      css=tbody>tr>td:nth-child(2)
    ${courses}=    create list
    FOR   ${ele}   IN   @{eles}
        log to console    ${ele.text}
        append to list    ${courses}   ${ele.text}
    END
    [Return]   ${courses}
