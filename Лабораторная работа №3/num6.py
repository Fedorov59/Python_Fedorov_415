'''
lab3.3 - 11.jpg  (Вариант 23)
'''

import math

n = float(input("Введите N: "));
x = float(input("Введите X: "));
i=1
sum=0


while(i<=n):
        sum=(math.pow(-1,i)*((math.pow(2*x,(i*2)))/(math.factorial(i*2))))+sum   
        i=i+1
print('Сумма ',n,' членов ряда равна ',sum)
