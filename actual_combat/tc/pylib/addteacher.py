from actual_combat.tc.pylib.courselib import *
from actual_combat.tc.pylib.teacherlib import *
import random
def addTeacher():
    #先添加一门课程
    coursename='python_'+str(random.randint(0,99999))
    addcourseobj=add_course(coursename,'pythond的课程','2')

    courseid=addcourseobj['id']
    #列出老师
    # teacherlist1=list_teacher()['retDict']

    #添加老师
    #courses的对象的格式[{"id":419,"name":"初中数学"},{"id":420,"name":"初中英语"}]
    username='teacher_'+str(random.randint(0,99999))


    addretobj=add_teacher(username,'123456','毕毕毕','老师描述',
                          [{"id":courseid,"name":coursename}],'2')
    if addretobj.get('retcode',None)==0:
        print('检查点返回结果recode为0，检查点通过')
    else:
        print('检查点返回结果recode不为0，检查点不通过')

    # teacherlist2=list_teacher()['retDict']
    if list_teacher()['id']==addcourseobj['id']:
        print('检查点在添加课程之后id是添加的课程的id，检查点通过 ！')
    else:
        print('检查点在添加课程之后id不是添加的课程的id，检查点不通过 ！')