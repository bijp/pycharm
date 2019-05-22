import time
from selenium import webdriver
def coursedel():
    driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://localhost/mgr/login/login.html')
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn-success').click()
    driver.implicitly_wait(1)
    while 1:
        delbtn=driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        time.sleep(2)
        if delbtn:
            delbtn[0].click()
            time.sleep(2)
            driver.find_element_by_class_name('btn-primary').click()
            time.sleep(1)
        else:
            break
    driver.implicitly_wait(10)
    driver.quit()
if __name__ == '__main__':
    coursedel()
