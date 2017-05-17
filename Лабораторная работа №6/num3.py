'''
lab11.3 - 16.jpg (Вариант 23)
'''

class student:
    def __init__(self):
        self.family=str()
        self.ball=float()
        self.cours=int()
    def volume(self):
        return(0.2*self.ball*self.cours)
    def info(self):
        print('Информация о студенте: ')
        print('Фамилия студента: ', self.family)
        print('Ср.Балл: %d' % (self.ball))
        print('Курс: %d \n' % (self.cours))

class discepline(student):
    def __init__(self):
        self.education=0
    def volume(self):
        if self.education=='да':
            return(0.2*self.ball*self.cours*2)
        else:
            return(0.2*self.ball*self.cours*0,9)

print('Демонстрация класса 1\n')
ivan=student()
a=input('Введите фамилию студента: ')
b=float(input('Ср.Балл: '))
c=int(input('Введите курс: '))
print()
ivan.family,ivan.ball,ivan.cours=a,b,c
ivan.info()
print('Качество студента: ',ivan.volume(),'\n')

print('Демонстрация класса 2\n')
andreev=discepline()
a=input('Введите фамилию студента: ')
b=float(input('Введите ср.балл: '))
c=int(input('Введите курс: '))
d=input('Изучает дисциплины на английском языке?: ')
print()
andreev.family,andreev.ball,andreev.cours,andreev.education=a,b,c,d
andreev.info()
print('Качество студента/2: ',andreev.volume(),'\n')
