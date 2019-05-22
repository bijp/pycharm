import pprint
fileid = 'C:/Users/Administrator/Desktop/logger_26_3_2019_14_1_3.csv'
listlines = open(fileid,'r')
lines1 = listlines.read().splitlines()
# pprint.pprint(lines1)
for line in lines1:
    data = 'HT-SIG:'
    if data in line:
        line = line.replace('(', '').replace(')', '').strip()
        lists1 = line.split(',')
        t=lists1[0]+','+lists1[5]+','+lists1[6]+','+lists1[7]+','+lists1[8]
        # pprint.pprint(t)
        if lists1[6]=='1830' and lists1[7]=='3' and lists1[8]=='1' :
            pprint.pprint(t)
            print('---------回复BA----------')
        else:
            print('--------条件不成立--------')

