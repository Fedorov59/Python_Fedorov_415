'''
lab3.1 - 2.jpg (Вариант 23)
'''

import math
n=float(input("Введите N : "))
sum=1
array=[]
i=1
while i<=n:
    array.append(i)
    i=i+1
for j in array:
    if(j==n):
        print("два в N степени равно ",2**n)
    sum=sum*(j)
print("n! = ",sum)
        
