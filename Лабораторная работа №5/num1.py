'''
lab4.1 - 2.jpg (Вариант 23)
'''
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

print("Введите значения массива : ")
suma=0
razn=1
array=[]
i=1
while i-1<=(13):
    print(i,' элемент массива :', end=' ')
    array.append(input())
    i=i+1
cls()
print(array)
i=1
while i-1<=(13):
    if(i%2==0):
        suma=suma+int(array[i-1])
    else:
        razn=razn*int(array[i-1])
    i=i+1
print('сумма чётных индексов ',suma)
print('произведение нечетных элементов ',razn)
        
