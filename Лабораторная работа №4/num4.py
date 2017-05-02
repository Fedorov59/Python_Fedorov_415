'''
lab4.1 - 7.jpg (Вариант 23. задание 9.174) 
'''

def sortByLength(inputStr):
    return len(inputStr)

s1=input("Введите предложение: ")
s2=[]
i=0
y=0
sum=0
s2.append([])
while i<=(len(s1)-1):
    if(s1[i]!=' '):
        s2[y].append(s1[i])
    else:
        s2.append([])      
        y=y+1
    i=i+1

print(s2)

print(' ')

s2.sort(key=sortByLength)

print(s2)
