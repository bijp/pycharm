import sys
from random import randint
from webapi import login,add_course,list_course
# 先登录
loginret,cookies = login('auto','sdfsdfsdf')

if loginret['retcode']==0:
    print('返回结果为0')
else:
    print('返回结果不为0')
    sys.exit()
sessionid =cookies['sessionid']

name_dix=randint(0,999999999)

print('.....先创建一门课程......')
coursename=f"大学物理课程_{name_dix}"
retobj=add_course(coursename,"大学物理课程的描述情况","5",sessionid)
if retobj['retcode']==0:
    print('返回结果为0')
else:
    print('返回结果不为0')
    sys.exit()
courseid=retobj['id']

print('列出课程，看下有没有新创建的课程')
retobj = list_course(sessionid)
retList=retobj['retlist']
expected={'desc': '大学物理课程的描述情况',
              'display_idx': 5,
              'id': courseid,
              'name': coursename}
if retList.count(expected)==1:
    print('返回结果包含新创建课程')
elif retList.count(expected)==0:
    print('返回结果不包含新创建课程')
else:
    print('返回结果包含多次新创建课程')
    sys.exit(3)
print('\n========= 用例 case001 通过 =============')

