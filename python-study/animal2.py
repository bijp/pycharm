class Animal :
    type = 'a'
    def __init__(self,name,weight,roomNum):
        self.name = name
        self.weight = weight
        self.roomNum = roomNum
    def roar(self):
        self.weight -= 5
        if self.name == 'tiger':
            print('Wow !!')
        if self.name == 'sheep':
            print('mie~~')
    def eat(self,food):
        print('之前的体重是' + str(self.weight))
        if (self.name == 'tiger' and food == 'meat') or (self.name == 'sheep' and food == 'grass'):
            self.weight += 10
            print('喂了'+self.name+'吃'+food+','+'体重增加了10,现在体重是'+str(self.weight))
        else :
            self.weight -= 10
            print('喂了' + self.name + '吃' + food + ',' + '体重减少了10,现在体重是' + str(self.weight))
    @staticmethod
    def run():
        print(Animal.type)
        print('run')



from random import randint

roomLen = 0
room = {}

while(roomLen < 10) :
    roomLen += 1
    if randint(1,2) % 2 == 0 :
        room[roomLen] = Animal('tiger',randint(180,250),roomLen)
    else:
        room[roomLen] = Animal('sheep',randint(120,200),roomLen)

roomno = randint(1,10)


room[1].run()


# ch = input('我们来到了房间# %s, 要敲门吗?[y/n]' % roomno)
# if ch == 'y':
#     room[roomno].roar()
# food = input('请给房间里面的动物喂食:')
# room[roomno].eat(food)


