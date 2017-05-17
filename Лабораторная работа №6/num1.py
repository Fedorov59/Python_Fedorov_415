'''
lab11.1 - 2.jpg and lab11.2 - 7.jpg(Вариант 23)
'''
import math

class Rast:
    def __init__(self):
        self.x1=int()
        self.y1=int()
        
    def info(self):
        print('Название класса: Rast')
        print('Значение атрибута x1: ',self.x1)
        print('Значение атрибута y1: ',self.y1)
        
    def TotalRast(self):
        return(math.sqrt((self.x1*self.x1)+(self.y1*self.y1)))

class Okr(Rast):
    def __init__(self):
        self.r=int()
        
    def Okru(self):
        if(self.TotalRast()<=self.r):
            return("yes")
        else:
            return("no")
    

c=Rast()
d=Okr()
edit=[]
edit.append(int(input('Введите координату x1: ')))
edit.append(int(input('Введите координату y1: ')))
c.x1, c.y1 = edit
memo=c.TotalRast()
print('Расстояние от точки до начала координат: ',memo)

print(' ')
edit=[]
edit.append(int(input('Введите координату x1: ')))
edit.append(int(input('Введите координату y1: ')))
edit.append(int(input('Введите радиус окружности: ')))
d.x1, d.y1, d.r = edit
memo=[d.TotalRast(), d.Okru()]
print('')
print('Расстояние от точки до начала координат: ',memo[0],'\nВходит ли точка в радиус окружности :  ',memo[1])
