'''
lab4.1 - 3.jpg (Вариант 23. задание 3) 
'''

s1=input("Введите 1 строку: ")
s2=input("Введите 2 строку: ")
s3=[]
i=0
y=0
sum=0
while i<=(len(s1)-1):
    while y<=(len(s2)-1):
        if(s1[i]==s2[y]):
            sum=sum+1
        y=y+1
    if(sum==0):
        s3.append(s1[i])
    y=0
    i=i+1
    sum=0

i=0
print('новая строка', end=' ')
while i<=(len(s3)-1):
    print(s3[i],end='')
    i=i+1
