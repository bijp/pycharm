#    登录网站https://www.vmall.com/index.html
 #    获得所有热销单品的名称，打印在log报表中

*** Settings ***
Library  SeleniumLibrary


*** Settings ***
华为商城热销单品
    Open Browser    https://www.vmall.com/index.html    chrome
    Set Selenium Implicit Wait 4
    ${eles}=         Get Webelements         css=.span-968 .grid-list .grid-items .thumb  .grid-title
    :FOR            ${ele}      IN      @{eles}
    \   log to console      ${ele.text}
