a=int(input("Введите a "))
b=int(input("Введите b "))
c=int(input("Введите c "))

if ((a+b)>c) and ((a+c)>b) and ((b+c)>a) and (a>0) and (b>0) and (c>0):
	print("треугольник существует")
else:
	print("треугольник не существует")
