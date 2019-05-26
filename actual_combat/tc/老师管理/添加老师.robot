*** Settings ***
Library   SeleniumLibrary
Library   Collections
Library   addteacher
Library   teacherlib
Library   courselib
Resource  ky.robot
*** Test Cases ***
添加老师
    ${listcourse}=    addcourse
    log to console  添加老师完成