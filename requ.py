import requests
import threading
#先创建同样个数的元素占位
listrequ=['','']
#控制对象listrequ
lock = threading.Lock()
def requ_mult():
    print('数为6的线程')
    r = requests.get('http://mirrors.163.com/centos/6/isos/x86_64/README.txt')
    #上锁和解锁
    lock.acquire()
    listrequ[0] = r.text
    lock.release()

def requ_mult2():
    print('数为7的线程')
    r2 = requests.get('http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt')
    lock.acquire()
    listrequ[1] = r2.text
    lock.release()


if __name__ == '__main__':
    print('主函数的线程')
    #创建线程
    t1 = threading.Thread(target=requ_mult, args=())
    t2 = threading.Thread(target=requ_mult2, args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(listrequ)
    fo = open('C:/Users/Administrator/Desktop/readme89.TXT', 'w')
    fo.write(''.join(listrequ))#数组转字符串
