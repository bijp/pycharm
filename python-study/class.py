class People :
    type = '高智慧灵长类动物'
    def __init__(self,name,height,sex,weight):
        self.height = height
        self.name = name
        self.sex =  sex
        self.weight = weight
    def getSex(self):
        print(self.sex)
    @staticmethod
    def getType():
        print(People.type)


class YelloPeople(People) :
    face = 'yello'
    def __init__(self,tf,name,height,sex,weight):
        People.__init__(self,name,height,sex,weight)
        self.tf = tf
    def getFace(self):
        print(YelloPeople.face)



hesy = YelloPeople('黑','hesy','171','男','160')

hesy.getFace()
hesy.getSex()