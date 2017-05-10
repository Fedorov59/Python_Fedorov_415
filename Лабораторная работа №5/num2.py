'''
lab4.1 - 5.jpg (Вариант 23)
'''

import os
import math

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

print("Введите значения массива X : ")
chis=1
snam=1
x=[]
y=[]
i=1
while i-1<=(9):
    print(i,' элемент массива :', end=' ')
    x.append(input())
    i=i+1
cls()
i=0
while i<=(9):
    yz=math.pow(int(x[i]),2)+0.3
    y.append(yz)
    i=i+1
cls()
print('массив X',x)
print('массив Y',y)
i=0
while i<=(9):
    if(i%2==0):
        snam=int(x[i])*float(y[i])*snam
    else:
        chis=int(x[i])*float(y[i])*chis
    i=i+1
print(chis)
print(snam)
print('P= ',chis/snam)

