a=int(input("Введите интервал a "))
b=int(input("Введите интервал b "))
c=int(input("Введите остаток c "))
d=int(input("Введите делитель d "))

for i in range(a, b+1):
	if (i%d==c):
		print(i,"")
 
