import requ,pprint
from cfg import *
import cfg

def login(username,password):
    payload = {
        'username': username,
        'password': password
    }
    # data参数 就是构造消息体的
    response = requ.post(httpBaseUrl("/api/mgr/loginReq"),
                         data=payload)

    # 获取结果，返回给调用者
    retDict = response.json()
    # 打印出结果
    print(retDict)

    return retDict,response.cookies


def add_course(name,desc,displayidx,sessionid):
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


    reponse = requ.post(f"http://{cfg.HOST}/api/mgr/sq_mgr/",
                        data=pl,
                        cookies={'sessionid': sessionid})

    retDict = reponse.json()

    print(retDict)
    return retDict


def list_course(sessionid):
    params = {
        'action':'list_course',
        'pagenum':'1',
        'pagesize':20
    }

    response = requ.get(f"http://{cfg.HOST}/api/mgr/sq_mgr/", params=params,
                        cookies={'sessionid': sessionid})
    # 获取结果，返回给调用者
    retDict = response.json()
    pprint.pprint(retDict)
    return retDict



def modify_course(courseid,name,desc,displayidx,sessionid):
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


    reponse = requ.put(f"http://{cfg.HOST}/api/mgr/sq_mgr/",
                       data=pl,
                       cookies={'sessionid': sessionid})

    retDict = reponse.json()

    print(retDict)
    return retDict


def delete_course(courseid,sessionid):
    payload = {
        'action': 'delete_course',
        'id': f'{courseid}'
    }

    response = requ.delete(f"http://{cfg.HOST}/api/mgr/sq_mgr/",
                           data=payload,
                           cookies={'sessionid': sessionid})

    r = response.json()
    pprint.pprint(r)
    return r

