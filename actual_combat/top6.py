"""定义一个python类IOString，有两个成员方法get_String 和 print_String
get_String 获取用户输入
print_String 将获取的输入信息大写输出
请写出类的实现，并分别调用这两个方法"""

class IOString():
    def __init__(self):
        self.inpu=''
    def get_String(self):
        self.inpu=input('请输入信息：')

    def print_String(self):
        t=self.inpu
        print(t.upper())
if __name__ == '__main__':
    ios = IOString()
    ios.get_String()
    ios.print_String()