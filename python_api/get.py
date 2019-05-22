import requ
import time
# import json
url='http://localhost/apijson/mgr/sq_mgr/'
# herders={'Content-Type','application/json'}

def add_course(name, desc, display_inx):
    name='大学物理课程'
    payload = {
        'action': 'add_course_json',
        'data':
            {
                "name":"%s",
                "desc":"%s",
                "display_inx":"%s"
            } % (name, desc, display_inx)

    }
    # return payload
    res1 = requ.post(url, json= payload)
    retDi=res1.json()
    print(retDi)
    return retDi
import pprint
def list_course(sessionid):
    params = {
        'action': 'list_course',
        'pagenum': '1',
        'pagesize': 20
    }
    response = requ.get(url, params=params)
    # 获取结果，返回给调用者
    retDict = response.json()
    pprint.pprint(retDict)
    return retDict



