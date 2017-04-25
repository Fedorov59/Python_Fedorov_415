'''
lab3.2 - 7.jpg (Вариант 23)
'''

import math 
n=float(input("Введите N : "))
i=2
sum=0
j=1

while(i<=n):
    while(j<=n):
        if(i%j==0):
            sum=sum+1
        j=j+1
    if(sum==2):
        print(i)
    sum=0
    j=1
    i=i+1
