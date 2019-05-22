dufile='C:/Users/bijp/Desktop/file1.txt'
fo=open(dufile,'r')
dufile2='C:/Users/bijp/Desktop/file2.txt'
fo2 = open(dufile2,'w')
fu1=fo.read().split('\n')
for i in fu1:
            namePart,salaryPart=i.split(';')
            name = namePart.split(':')[1].strip() #去除头部或者尾部的空格
            salary = int(salaryPart.split(':')[1].strip())
            income = int(salary*0.9)
            tax = int(salary * 0.1)
            wf=' name:{:8}; salary:{:8}; tax:{:6}; income:{:6}'.format(name,salary,tax,income)
            print (wf)
            fo2.write(wf+'\n')

