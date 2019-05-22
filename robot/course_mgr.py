import requests
import pprint
def listCourse():
    params = {
        'action':'list_course',
        'pagenum':'1',
        'pagesize':20
    }
    response = requests.get(f"http://localhost/api/mgr/sq_mgr/", params=params)
    # 获取结果，返回给调用者
    retDict = response.json()
    pprint.pprint(retDict)
    #返回课程列表的课程名字
    return [ one['name']  for one in  retDict["retlist"]]

if "__main__"==__name__:
    cnamelist=listCourse()
    for one in cnamelist:
        print(one)
