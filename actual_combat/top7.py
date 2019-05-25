"""访问天气预报接口http://www.weather.com.cn/data/sk/101190408.html
返回城市名和温度，对应的字段分别是city和temp
要求使用requests模块，返回信息不能是乱码"""

import requests

url='http://www.weather.com.cn/data/sk/101190408.html'
rep=requests.get(url)
rep.encoding='utf-8'
u=rep.text
#字符串转换字典
s_dic = eval(u)
city=s_dic['weatherinfo']['city']
weath=s_dic['weatherinfo']['temp']
# print('城市:%s' % city)
# print('温度:%s' % weath)
print("%s:%s" % ( city,weath))

