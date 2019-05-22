'''1. 访问天气查询网站（网址如下），查询江苏省天气
http://www.weather.com.cn/html/province/jiangsu.shtml

2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
温度最低为12℃, 城市有连云港 盐城 '''
from selenium import webdriver

driver=webdriver.Chrome('D:\seleniumtool\chromedriver_win32v73\chromedriver.exe')

#打开江苏天气页面
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
weatherlist=driver.find_element_by_id('forecastID')
# print(weatherlist.text)

weatherlist2=weatherlist.text.split(u'℃\n')
# print(weatherlist2)
lowwea=50

listcity=[]
for one in weatherlist2:
    citycur=one.replace(u'\n',',').replace('℃/',',').replace('℃','')
    # print(citycur)
    city=citycur.split(',')[0]
    lowweather=int(citycur.split(',')[1])
    highweather=int(citycur.split(',')[2])
    if lowweather<lowwea:
        lowwea=lowweather
        listcity.append(city)
        # listcity=[city]
    elif lowweather==lowwea:
        listcity.append(city)
#温度最低为12℃, 城市有连云港 盐城
print('温度最低的城市是%s,城市都有%s' % (lowwea,' '.join(listcity)))
driver.close()



