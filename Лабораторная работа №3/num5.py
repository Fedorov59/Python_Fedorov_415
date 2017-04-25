'''
lab3.2 - 10.jpg  (Вариант 23)
'''

import math
import random
arr1=[]
arr2=[]
arr3=[]
arr4=[]

i=1
n=10
umn1=1
umn2=1
while(i<=n):
    arr1.append(random.randint(1,9))
    i=i+1
i=1
while(i<=n):
    arr2.append(random.randint(1,9))
    i=i+1
i=0
while(i<=n-1):
    umn1=arr1[i]*arr2[i]
    arr3.append(umn1)
    i=i+1
i=0
while(i<=n-1):
    print(arr1[i]," * ",arr2[i]," = ", end=' ')
    umn2=float(input())
    arr4.append(umn2)
    i=i+1
i=0
sum=0
while(i<=n-1):
    if(arr3[i]==arr4[i]):
        sum=sum+1
    i=i+1
if(sum==10):
    print("Оценка Отлично")
if(sum<10 and sum>7):
    print("Оценка Хорошо")
if(sum<=7 and sum>=6):
    print("Оценка Удовлетворительно")
if(sum<6):
    print("Оценка Плохо")

