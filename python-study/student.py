
funne= input('请输入学生相关信息:')
sttmanege = funne.split(';')
for i in sttmanege:
    if ',' not in i:
        continue

    name, age = i.split(',')
    name=name.strip() #去除头尾部空格
    age=age.strip()
    if not age.isdigit():
        continue
    age=int(age)
    print('%-20s : %02d' % (name,age))