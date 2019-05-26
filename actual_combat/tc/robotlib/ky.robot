*** Settings ***
Library   SeleniumLibrary
Library   Collections
Library   teacherlib
Library   courselib
Library  addteacher
*** Keywords ***
loginwebsite
    [Arguments]     ${username}       ${password}
    open web
    input text      id=username         ${username}
    input text      id=password         ${password}
    click element   css=.btn-success
addcourse
    add_course
GetCourseList
    list_teacher
open web
    open browser    http://localhost/mgr/login/login.html   chrome
    set browser implicit wait  10
close web
    close browser

setup web
    open web
    loginwebsite    auto        sdfsdfsdf
    delete_teacher
    delete_course
teardown web
    close web
    delete_teacher
    delete_course