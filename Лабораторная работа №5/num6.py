'''
lab4.2 - 14.jpg (Вариант 23) 
'''

import os
import math
from random import randint

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

cls()

n=5
matrix = [[0 for j in range(n)] for i in range(n)]


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print()

suma=0
print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(i==(int(n/2))) or (j==(int(n/2))):
            matrix[i][j]=1
            
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
    print()


