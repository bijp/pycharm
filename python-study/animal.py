
class Room:#编号、动物
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal
class Tiger(self):

r1 = Room(1,t1)
print(r1.num,r1.animal)
# # 描述这个房间r1的动物的roar()
r1.animal.roar()
print(t1.weight)

#取随机数
from random import randint
print(randint(0,2))#0 1, 2  双闭区间
# #初始化随机取动物  --10个房间实例--保存--列表
roomList = []
for one in range(1,11):#10个
    if randint(0,1) == 1:
        ani = Tiger(200)
    else:
        ani = Sheep()
    room = Room(one,ani)
    roomList.append(room)
    class Tiger:
        classname='老虎'
    class Roar():

        def roar(self):  # 叫
            self.weight -= 5
            print('WOW!', '---体重减5斤！')

        def feed(self, food):  # 喂食
            if food == '肉':
                self.weight += 10
                print('喂食正确，体重增加10斤！')
            else:
                self.weight -= 10
                print('喂食错误，体重减少10斤！')
'''如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤

如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。


游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。 
游戏3分钟结束后，显示每个房间的动物和它们的体重。
'''

