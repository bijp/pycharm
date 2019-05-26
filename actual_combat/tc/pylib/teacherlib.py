import requests
from actual_combat.tc.cfg import *
import json
#添加老师
def add_teacher(username,password,realname,desc,courses,display_idx):
    pl = {
        'action': 'add_course',
        'data' :f'''
                {{
                  "username":"{username}",
                  "password":"{password}",
                  "realname":{realname},
                  "desc":"{desc}",
                  "courses":{json.dumps(courses)},
                  "display_idx":{display_idx}
                }}
        '''
    }

    print(pl)
    reponse =requests.post(f"http://{HOST}/api/mgr/sq_mgr/",
                        data=pl)
    retDict = reponse.json()
    return retDict

#列出老师
def list_teacher():
    params = {
        'action':'list_teacher',
        'pagenum':'1',
        'pagesize':20
    }
    response = requests.get(f"http://{HOST}/api/mgr/sq_mgr/", params=params)
    # 获取结果，返回给调用者
    retDict = response.json()
    return retDict

#修改老师
def modify_teacher(teacherid,username,password,realname,desc,courses,display_idx):
    pl = {
        'action': 'modify_teacher',
        'id' : teacherid,
        'data' : f'''
                {{
                  "username":"{username}",
                  "password":"{password}",
                  "realname":"{realname}",
                  "desc":"{desc}",
                  "courses":{json.dumps(courses)},
                  "display_idx":"{display_idx}"
                }}
        '''
    }
    reponse = requests.put(f"http://{HOST}/api/mgr/sq_mgr/",
                       data=pl )

    retDict = reponse.json()
    return retDict

#删除老师
def delete_teacher(teacherid):
    payload = {
        'action': 'delete_teacher',
        'id': f'{teacherid}'
    }
    response = requests.delete(f"http://{HOST}/api/mgr/sq_mgr/",
                           data=payload)
    r = response.json()
    return r
