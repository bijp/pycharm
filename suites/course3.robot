*** Settings ***
Library   SeleniumLibrary
Library   Collections
Library   deleteAllCourse
*** Test Cases ***
课程添加用例
    [Setup]    coursedel
    [Teardown]  coursedel
    open browser    http://localhost/mgr/login/login.html   chrome
    set browser implicit wait  10
    input text      id=username         auto
    input text      id=password         sdfsdfsdf
    click element   css=.btn-success
    click element   css=[ng-click="showAddOne=true"]

    input text      css=[ng-model="addData.name"]   robot
    input text      css=[ng-model="addData.desc"]   robotdesc
    input text      css=[ng-model="addData.display_idx"]   1

    click element    css=[ng-click="addOne()"]
    sleep   3
    ${courseneme}    Get WebElements                css=tbody>tr>td:nth-child(2)
#    FOR  ${ele}  IN   @{courseneme}
#        log to console  ${ele.text}
#    END
   ${lessons}=    create list
    :FOR   ${ele}   IN   @{courseneme}
       \   log to console    ${ele.text}
       \   Append To List   ${lessons}   ${ele.text}

    ${expected}=   create list    robot
    Lists Should Be Equal    ${lessons}     ${expected}
    close browser






