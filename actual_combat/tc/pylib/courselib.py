import requests
from actual_combat.tc.cfg import *
#添加课程
def add_course(name,desc,displayidx):
    pl = {
        'action': 'add_course',
        'data' : '''
                {
                  "name":"%s",
                  "desc":"%s",
                  "display_idx":"%s"
                }
        ''' %  (name,desc,displayidx)
    }
    reponse = requests.post(f"http://{HOST}/api/mgr/sq_mgr/",
                        data=pl)
    retDict = reponse.json()
    return retDict

#列出课程
def list_course():
    params = {
        'action':'list_course',
        'pagenum':'1',
        'pagesize':20
    }
    response = requests.get(f"http://{HOST}/api/mgr/sq_mgr/", params=params)
    # 获取结果，返回给调用者
    retDict = response.json()
    return retDict

#修改课程
def modify_course(courseid,name,desc,displayidx):
    pl = {
        'action': 'modify_course',
        'id' : courseid,
        'data' : f'''
                {{
                  "name":"{name}",
                  "desc":"{desc}",
                  "display_idx":"{displayidx}"
                }}
        '''
    }
    reponse = requests.put(f"http://{HOST}/api/mgr/sq_mgr/",
                       data=pl )

    retDict = reponse.json()
    return retDict

#删除课程
def delete_course(courseid):
    payload = {
        'action': 'delete_course',
        'id': f'{courseid}'
    }
    response = requests.delete(f"http://{HOST}/api/mgr/sq_mgr/",
                           data=payload)
    r = response.json()
    return r
