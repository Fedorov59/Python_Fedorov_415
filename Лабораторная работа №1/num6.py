'''
lab01 - 15.jpg  (Вариант 23)
'''

import math

n=0
while (n <= 1):
	n = float(input("Введите N:"));

u = math.sqrt(n/(n+1))
t = math.acos(u)/(2*math.pi)
print('u/U(max) :'+str(u))
print('t/T :'+str(t))
