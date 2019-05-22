from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import  Select
driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.implicitly_wait(15)
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@id="date_range"]/ul/li[2]').click()
# time.sleep(2)
#出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’
driver.find_element_by_xpath('//*[@id="fromStationText"]').click()
driver.find_element_by_xpath('//*[@id="fromStationText"]').clear()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="fromStationText"]').send_keys('南京南')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="fromStationText"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="toStationText"]').click()
driver.find_element_by_xpath('//*[@id="toStationText"]').clear()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="toStationText"]').send_keys('杭州东')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="toStationText"]').send_keys(Keys.ENTER)
time.sleep(3)
# 注意输入城市名前，一定要先点击一下输入框，否则查不到,而且输入城市名最后要包含一个回车符，否则输入框里面会自动清除

#发车时间 选 06:00--12:00,发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('06:00--12:00')

driver.find_element_by_xpath('//*[@id="date_range"]/ul/li[2]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="query_ticket"]').click()

'''我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息（这里可以用xpath），结果如下：

G7641
G1505
G7393
G7689'''

print('\n\n\n===============先查询有二等座的，再从二等座返回前面的路径的车次================\n\n\n')
#//*[@id="queryLeftTable"]//td[4][@class]查找是否有票，有票则返回到车次目录/../td[1]//a
theTrains = driver.find_elements_by_xpath('//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a')
for one in theTrains:
    print (one.text)
# Trains=driver.find_elements_by_xpath('//*[@id="queryLeftTable"]/tr')
# for Train in Trains:
#     t=Train.find_element_by_xpath('./td[4]')
#       if t.text=='有' or t.text.isdigit():
#           TrainName=Train.find_element_by_xpath('./following-sibling::tr[1]').get_attribute('datatran')
#           print(t)



driver.quit()


