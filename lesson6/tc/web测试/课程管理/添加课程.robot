*** Settings ***
Library   SeleniumLibrary
Library   Collections
Library   deleteAllCourse
Resource   ky.robot

*** Test Cases ***
课程添加用例1
    [Setup]    coursedel
    [Teardown]  coursedel
    loginwebsite       auto        sdfsdfsdf
    set browser implicit wait  10
    addcourse     robot1    robot1desc      1
    ${course}=   GetCourseList
    Should Be True   $course==['robot1']
    close browser
课程添加用例2
    [Setup]    coursedel
    [Teardown]  coursedel
    loginwebsite       auto        sdfsdfsdf
    set browser implicit wait  10
    addcourse       python      pythondesc      2
    ${course}=   GetCourseList
    Should Be True   $course==['python']
    close browser
