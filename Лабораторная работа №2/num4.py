'''
lab2.2 - 11.jpg (Вариант 23)
'''

import math 
x=float(input("Введите скорость в км/ч : "))
y=float(input("Введите скорость в м/с : "))

z=x

x=(x*1000)/3600
if x>y:
    print(z," км/ч больше чем ",y," м/с")
else:
    print(y," м/c больше чем ",z," км/ч")
