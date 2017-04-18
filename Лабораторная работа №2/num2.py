'''
lab2.1 - 5.jpg (Вариант 23)
'''


dt=float(input("Продолжительность разговора в минутах : "))
s=float(input("Стоимость минуты разговора 0.90 или 0.35 : "))
d=float(input("День недели от 1 до 7: "))

if (s==0.90):
    if ((d>=6) and (d<=7)):
        st=dt*s
        st=st-st*0.1
    else:
        st=dt*s      
else:
    if ((d>=6) and (d<=7)):
        st=0.35*dt
        st=st-st*0.1
    else:
        st=dt*s
print('Стоимость разговора ='+str(st))
