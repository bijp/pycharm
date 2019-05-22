*** Settings ***
Library    SeleniumLibrary
Library    course_mgr
Library    Collections

*** Test Cases ***

华为商城热销单品
    Open Browser    https://www.vmall.com/index.html    chrome
    Set Selenium Implicit Wait      4
    @{eles}=        Get WebElements          css=.span-968>.grid-list>.grid-items>.thumb >.grid-title
    :FOR            ${ele}      IN      @{eles}
    \   log to console      ${ele.text}
#    \   ${eletxt}=   evaluate  $ele.get_attribute('innerText')
#       \   log to console   ${eletxt}
    Close Browser