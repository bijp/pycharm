import time,paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.199.209",22333,"root", "sdfsdf")

def getcontent(lines,fieid):
    for line in lines:
        if fieid in line:
            value=line.split(':')[1].split('kb')[0].strip()
            return int(value)

count = 0
while True:
    count += 1

    with open('/proc/meminfo') as f:
        beginlines = f.readlines()[:8]

    memTotal = getcontent(beginlines,'MemTotal')
    memFree  = getcontent(beginlines,'MemFree')
    buffers  = getcontent(beginlines,'Buffers')
    cached   = getcontent(beginlines,'Cached')

    # print memTotal,memFree,buffers,cached
    # 别忘了 * 100
    memUsage = (memFree + buffers + cached) *100.0/memTotal
    # 搜索时间格式
    memUsage = '%s     %.2f%%' % (time.strftime('%Y%m%d_%H:%M:%S'),memUsage)
    print(memUsage)

    with open('ret.txt','a') as f:
        f.write(memUsage+'\n')

    time.sleep(5)

    # 防止一直运行
    if count>15:
        break