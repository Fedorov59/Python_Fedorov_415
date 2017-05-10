'''
lab4.2 - 11.jpg (Вариант 23) 
'''

import os
import math
from random import randint

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

cls()

n=int(input('Размерность матрицы: '))
minn=n
    
matrix = [[randint(1,9) for j in range(n)] for i in range(n)]


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print()

suma=0
print()

for j in range(len(matrix)):
    for i in range(len(matrix[j])):
        suma=0
        if(i or j):
            if(int(matrix[i][j])%(i+j)==0):
                suma=suma+1
    if((suma<minn) and (suma>0)):
        minn=suma
        st=j
        
suma=int(suma/20)
print('среднее арифметическое значение: ',st, minn)
        

