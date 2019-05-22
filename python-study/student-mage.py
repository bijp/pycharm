Mo='C:/Users/Administrator/Desktop/0005_1.txt'
import re

print()

fo=open(Mo,'r')
fu1=fo.read().splitlines()

print (re.sub(r'[(|)]','',fu1[1].strip()))
dw={}
maneger={}
# for i in fu1:
#     checkintime1,lessonid1,studentid1=i.split(',')
#     print (checkintime1)
    # maneger = {'lessonid':lessonid1 ,'checkintime':checkintime1}
    # dw={'studentid1':[maneger]}
    # if studentid1 in list:
    #     dw.append('studentid1':[maneger])
