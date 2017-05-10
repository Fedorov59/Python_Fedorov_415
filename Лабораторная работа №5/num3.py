'''
lab4.1 - 7.jpg (Вариант 23)
'''

import os
import math

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

cls()
   
n=input("Введите количество элементов двоичного массива : ")
print("Введите значения двоичного массива : ")
suma=0
x=[]


i=0
while i<=int(n)-1:
    print(i,' элемент массива :', end=' ')
    x.append(input())
    i=i+1

MIN = min(x)
MAX = max(x)
MAX_INDEX = x.index(MAX)+1
MIN_INDEX = x.index(MIN)+1
print('MAX: ', MAX)
print ('MIN: ', MIN)

if(MAX_INDEX>MIN_INDEX):
    suma=MAX_INDEX-MIN_INDEX
    if(suma>1):
        print('количество элементов: ',suma-1)
    else:
        print('элементов нет')
else:
    suma=MIN_INDEX-MAX_INDEX
    if(suma>1):
        print('количество элементов: ',suma)
    else:
        print('элементов нет')



