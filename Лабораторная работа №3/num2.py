'''
lab3.1 - 3.jpg (Вариант 23)
'''
import math
n=float(input("Введите N: "))

s=0
fact=1
array=[]
i=1
while i<=n:
    array.append(i)
    i=i+1
for j in array:
    fact=fact*j
    if(j-4)!=0:
        sum=(((j-4)**3)*(j+7))/fact
        s=s+sum
print('S ='+str(s))
