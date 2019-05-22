*** Settings ***
Library    SeleniumLibrary
Library    course_mgr
Library    Collections
*** Test Cases ***
测试课程列表
    ${listcourse}=             listCourse
    :FOR        ${ele}       IN      @{listcourse}
      \         log to console      ${ele}
      ${totalcourse}=            create list  大学物理    python   Selenium  23
      should be equal     ${listcourse}    ${totalcourse}


华为商城热销单品
    Open Browser    https://www.vmall.com/index.html    chrome
    Set Selenium Implicit Wait      4
    @{eles}=        Get WebElements          css=.span-968>.grid-list>.grid-items>.thumb >.grid-title
    :FOR            ${ele}      IN      @{eles}
    \   log to console      ${ele.text}
    Close Browser