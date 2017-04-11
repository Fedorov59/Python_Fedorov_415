'''
lab01 - 7.jpg (Вариант 23)
'''

import math 
y=float(input("Введите У : "))
d=float(input("Введите d : "))

r=((math.pow(math.sin(y),2)+0.3*d))
r=r/(math.exp(y)+math.log(d))   
print('r ='+str(r))
