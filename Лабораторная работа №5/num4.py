'''
lab4.2 - 9.jpg (Вариант 23) 
'''

import os
import math
from random import randint

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

cls()
    
matrix = [[randint(0,9) for j in range(5)] for i in range(4)]


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print()

suma=0
print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        suma=int(matrix[i][j])+suma
suma=int(suma/20)
print('среднее арифметическое значение: ',suma)
        
koll=0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(int(matrix[i][j])>suma):
            koll=koll+1
print('количество элементов матрицы, превосходящих ср.арифм.: ',koll)

