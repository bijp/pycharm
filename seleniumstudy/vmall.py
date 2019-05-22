from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')
driver.get('https://www.vmall.com/')
driver.implicitly_wait(10)
'''检查 "华为官网" 页面上是否 有如下主菜单

  智能手机
  笔记本
  平板
  穿戴设备
  智能家居
  更多产品
  软件应用
  服务与支持'''
driver.find_element_by_xpath('//*[@class="s-sub"]/ul/li[2]').click()
time.sleep(2)
vmall_handle1=driver.current_window_handle
#获取句柄
handels=driver.window_handles
# print(handels)
#循环遍历句柄
for handle in handels:
    driver.switch_to_window(handle)
    if "华为消费者业务官网" in driver.title:
        print("切进来华为官网了")
        break
handle2=driver.current_window_handle
driver.maximize_window()

expect='智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持'
t=driver.find_elements_by_xpath('//*[@class="left-box"]/ul/li/a')
ttexts = [i.text for i in t]
ttext='|'.join(ttexts)
# print(ttext)
if ttext == expect:
    print('华为官网验证成功！！！！！')
else:
    print('华为官网验证成失败！！！！！')

#最后再回到主窗口， 检查鼠标停留在 "笔记本&平板" 处的时候， 是否显示的菜单有"平板电脑  笔记本电脑 笔记本配件"
driver.switch_to_window(vmall_handle1)
#鼠标停留笔记本&平板处
stop=driver.find_element_by_xpath('//*[@id="zxnav_1"]')
ActionChains(driver).move_to_element(stop).perform()

t2=stop.find_elements_by_css_selector('#zxnav_1 .subcate-item a span')

t2text='平板电脑|笔记本电脑|笔记本配件'
eleTexts = [j.text for j in t2]
actual = '|'.join(eleTexts)
if actual == t2text:
    print('华为商城验证成功')
else:
    print('华为商城验证失败')
driver.quit()