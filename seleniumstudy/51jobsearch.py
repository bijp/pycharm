from selenium import webdriver
import time
from selenium.webdriver.support.ui import  Select
driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')

driver.get('http://www.51job.com')

driver.implicitly_wait(15)
#进入高级搜索
driver.find_element_by_css_selector('body > div.content > div > div.fltr.radius_5 > div > a').click()
#输入关键字
driver.find_element_by_css_selector('#kwdselectid').send_keys('python')

#选择地区杭州
driver.find_element_by_css_selector('#work_position_click > em').click()
time.sleep(2)
redcitys=driver.find_elements_by_css_selector('#work_position_click_multiple_selected span.ttag')
if redcitys==[]:
    pass
else:
    for redcity in redcitys:
        redcity.click()
#选择杭州这个城市
time.sleep(2)
driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_080200').click()
time.sleep(2)
driver.find_element_by_css_selector('#work_position_click_bottom_save').click()
# 要点一下别的地方， 否则下面的元素会被挡住
driver.find_element_by_css_selector('div.tit').click()
#选择职能类别
time.sleep(1)
driver.find_element_by_css_selector('#funtype_click').click()
time.sleep(1)
driver.find_element_by_css_selector('#funtype_click_center_right_list_category_0100_0100').click()
time.sleep(1)
driver.find_element_by_css_selector('#funtype_click_center_right_list_sub_category_each_0100_0106').click()
time.sleep(1)
driver.find_element_by_css_selector('#funtype_click_bottom_save').click()

#公司性质选 外资 欧美
m=driver.find_element_by_css_selector('#cottype_list')
m.find_element_by_css_selector('.ic').click()
m.find_element_by_css_selector('.ul .li:nth-child(2)').click()


#工作年限选 1-3 年
n=driver.find_element_by_css_selector('#workyear_list')
n.find_element_by_css_selector('.ic').click()
n.find_element_by_css_selector('.ul .li[data-value="02"]').click()

driver.find_element_by_css_selector('body > div.container > div.d_lt.Fm > div.btnbox.p_sou > span').click()
'''搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
    Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
    Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
'''
jobs=driver.find_elements_by_css_selector('#resultList div.el')[1:]
for job in jobs:
    job_postion=job.find_element_by_css_selector('#resultList .t1 a').text
    job_comp = job.find_element_by_css_selector('span.t2 a').text
    job_area = job.find_element_by_css_selector('span.t3').text
    job_salary = job.find_element_by_css_selector('span.t4').text
    job_date = job.find_element_by_css_selector('span.t5').text
    print('|'.join([job_postion,job_comp,job_area,job_salary,job_date]))

driver.quit()
'''登录 http://www.51job.com
    点击高级搜索
    输入搜索关键词 python 
    地区选择 杭州
    职能类别 选 计算机软件 -> 高级软件工程师
    公司性质选 外资 欧美
    工作年限选 1-3 年
    
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
 
    Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
    Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27

'''