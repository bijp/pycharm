import time

from selenium import webdriver
#打开电脑上的浏览器以手机模式运行
chrome_options=webdriver.ChromeOptions()
#选择一种存在的模拟 手机的设备类型
chrome_options.add_experimental_option(
    "mobileEmulation",{"deviceName":"iphone X"}
)
driver=webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())
driver.implicitly_wait(10)