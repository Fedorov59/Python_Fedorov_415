'''
lab01 - 8.jpg (Вариант 23)
'''

import math 
x=float(input("Введите x : "))
z=float(input("Введите z : "))
b=float(input("Введите b : "))
a=float(input("Введите a : "))
f=((math.sqrt(math.fabs(x)+math.pow(math.cos(x),3)+math.pow(z,4))))
f=f/(math.log(x)-math.asin(b*x-a))        
print('f = '+str(f))
