from selenium import webdriver
import time

driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')

driver.get('http://www.51job.com')
driver.implicitly_wait(15)
#输入关键字
driver.find_element_by_css_selector('#kwdselectid').send_keys('python')
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
driver.find_element_by_css_selector('#work_position_click_center_right_list_category_000000_080200').click()
driver.find_element_by_css_selector('#work_position_click_bottom_save').click()
driver.find_element_by_css_selector('.ush button').click()
jobs=driver.find_elements_by_css_selector('#resultList div.el')[1:]
# for i in jobs:
#     print(i.text)
for job in jobs:
    job_postion=job.find_element_by_css_selector('#resultList .t1 a').text
    job_comp = job.find_element_by_css_selector('span.t2 a').text
    job_area = job.find_element_by_css_selector('span.t3').text
    job_salary = job.find_element_by_css_selector('span.t4').text
    job_date = job.find_element_by_css_selector('span.t5').text
    print('|'.join([job_postion,job_comp,job_area,job_salary,job_date]))


driver.quit()