import requ
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
    reponse = requ.post('http://localhost/api/mgr/sq_mgr/',
                        data=pl,
                        cookies={'sessionid': sessionid})

    retDict = reponse.json()

    print(retDict)
    return retDict