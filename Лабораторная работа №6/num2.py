'''
lab11.1 - 5.jpg and lab11.2 - 11.jpg (Вариант 23)
'''


class chisla:
    def __init__(self, a=1, b=2, c=3, d=4):
        self.p=[float(a), float(b), float(c), float(d)]
    def __del__(self):
        print('Числа успешно удалены')
    def info(self):
        print('Информация об объекте:\nКласс: chisla\nТекущие атрибуты:\na=%.3f\nb=%.3f\nc=%.3f\nd=%.3f\n' % (self.p[0],self.p[1],self.p[2],self.p[3]))
    def sr_arifm(self):
        self.arifm=(self.p[0]+self.p[1]+self.p[2]+self.p[3])/4
        return(self.arifm)
    def maxx(self):
        maax=self.p[0]
        i=0
        while i<=3:
            if self.p[i]>maax:
                maax=self.p[i]
                i=i+1
            else:
                i=i+1
        return(maax)

class SumaKvChisel(chisla):
    def __init__(self, x=1):
        self.p2=[float(x)]
    def __del__(self):
        print('Объект успешно удален')
    def info(self):
        print('Информация об объекте:\nКласс: SumaKvChisel\nТекущие атрибуты:\na=%.3f\nb=%.3f\nc=%.3f\nd=%.3f\nx=%.3f\n' % (self.p[0],self.p[1],self.p[2],self.p[3],self.p2[0]))
    def summ(self):
        i=0
        su=0
        while i<=3:
            s=self.p[i]-self.p2[0]
            su=su+(s*s)
            i=i+1
        return(su)


print('Демонстрация родительского класса\n')
n=chisla()
edit=[]
for j in range(4):
    edit.append(float(input('Введите значение %s числа: ' % (chr(ord('a')+j)))))
print()
n.p= edit
n.info()
memo=[n.sr_arifm(), n.maxx()]
print('Среднее арифметическое: ',memo[0])
print('Максимальное число\n' ,memo[1])
del n
print()


print('Демонстрация класса-потомка\n')
o=SumaKvChisel()
edit=[]
edit.append([])
for j in range(4):
    edit[0].append(float(input('Введите значение %s числа: ' % (chr(ord('a')+j)))))
edit.append([])
edit[1].append(float(input('Введите значение %s числа: ' % (chr(ord('x'))))))
print()
o.p, o.p2 = edit
o.info()
memo=[o.sr_arifm(), o.maxx(), o.summ()]
print('Информация о числах объекта: ')
print('Среднее арифметическое: ',memo[0])
print('Максимальное число\n', memo[1])
print('Cумма квадратов разности числа: ',memo[2])
del o

