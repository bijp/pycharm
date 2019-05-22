from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://tinypng.com/')
# driver.maximize_window()
#上传图片按钮定位
driver.find_element_by_xpath('//*[@id="top"]/section/section/figure').click()
time.sleep(2)
import win32com.client
shell=win32com.client.Dispatch("WScript.Shell")
driver.implicitly_wait(15)
time.sleep(2)
#上传图片,//*[@id="top"]/section/section/figure
shell.Sendkeys(r"E:\20170721112352.png"+'\n')
print("-----图片上传成功-----")
driver.quit()

