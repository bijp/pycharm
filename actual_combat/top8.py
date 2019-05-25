"""请写一个程序，访问https://www.51job.com/
抓取关键字：测试开发，地点南京的工作中，前3页的职位中，前3页的职位中，月薪在15000元以上的工作 """

import time
from selenium import webdriver
import re
driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')
driver.get('https://www.51job.com/')
driver.implicitly_wait(15)
#输入关键字
driver.find_element_by_css_selector('#kwdselectid').send_keys('测试开发')
#选择城市，redcitys是已选择城市的遍历
driver.find_element_by_css_selector('#work_position_input').click()
time.sleep(1)
redcitys=driver.find_elements_by_css_selector('#work_position_click_multiple_selected span.ttag')

if redcitys==[]:
    pass
else:
    for redcity in redcitys:
        redcity.click()
#选择杭州这个城市
driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_070200').click()
driver.find_element_by_css_selector('#work_position_click_bottom_save').click()
driver.find_element_by_css_selector('.ush button').click()
def postion():
    jobs=driver.find_elements_by_css_selector('#resultList div.el')[1:]
    for job in jobs:
        # job_postion=job.find_element_by_css_selector('#resultList .t1 a').text
        # job_comp = job.find_element_by_css_selector('span.t2 a').text
        # job_area = job.find_element_by_css_selector('span.t3').text
        job_salary = job.find_element_by_css_selector('span.t4').text
        job_postion = job.find_element_by_css_selector('#resultList .t1 a').text
        if '万/月' in job_salary:
            salarymax1=job_salary.replace('-',',').replace('万/月','').split(',')[1]
            salarymax=float(salarymax1)
            if salarymax>=1.5:
                print(job_postion,job_salary)
        elif '年' in job_salary:
            salarymax2 = job_salary.replace('-', ',').replace('万/年', '').split(',')[1]
            salarymax=float(salarymax2)
            if salarymax>=15:
                print(job_postion,job_salary)
        elif '千' in job_salary:
            salarymax3 = job_salary.replace('-', ',').replace('千/月', '').split(',')[1]
            salarymax=float(salarymax3)
            if salarymax>=15:
                print(job_postion,job_salary)
        else:
            continue
# postion()
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
page=driver.find_element_by_css_selector('#resultList > div.dw_page > div > div > div > span:nth-child(2)')
pages=float(re.sub("\D", "", page.text))
if pages>3:
    pages=3
count = 0
while count<pages:
    postion()
    rtne=driver.find_elements_by_css_selector('#resultList > div.dw_page > div > div > div > ul > li:nth-child(4) > a')
    # print(len(rtne))
    if len(rtne)>0:
        rtne[0].click()
        count += 1
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
    else:
        count = 1000000000000








# rtne=driver.find_element_by_css_selector('#rtNext')
# if  rtne:
#     rtne.click()
#
    # job_date = job.find_element_by_css_selector('span.t5').text
    # print('|'.join([job_postion,job_comp,job_area,job_salary,job_date]))


driver.quit()


#resultList > div.dw_page > div > div > div > ul > li:nth-child(4) > span