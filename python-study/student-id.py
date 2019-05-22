fileid='C:/Users/Administrator/Desktop/studentbijieping/0005_1.txt'
listlines=open(fileid,'r')
lines1=listlines.read().splitlines()
# print (lines1)
list1 = {}
maneger = {}
for lin in lines1:
            lin = lin.replace('(', '').replace(')', '').replace(';', '').strip()
            # print (lines)
            lists1=lin.split(',')
            # print(lists1)
            checkintimeone=lists1[0].replace("'",'').strip()
            # print (checkintimeone)
            lessonidone = int(lists1[1].strip())
            studentidone = int(lists1[2].strip())

            maneger={'lessonid':lessonidone,'checkintime':checkintimeone}
            list = {studentidone: [maneger]}
            # list['studentid']=studentidone
            if studentidone not in list1:
                        list1[studentidone] = []
                        list1[studentidone].append(maneger)
            else:
                        list1[studentidone].append(maneger)
# print(list1)
import pprint
pprint.pprint(list1)
