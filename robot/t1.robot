*** settings ***
Library  SeleniumLibrary

*** Test Cases ***
百度搜索松勤
    open Browser                http://www.baidu.com        chrome
    set browser implicit wait   5
    input text                  id=kw                       松勤\n
    ${fristRet}=                get text                    id=1
    should contain              ${fristRet}                 松勤网
    Close browser