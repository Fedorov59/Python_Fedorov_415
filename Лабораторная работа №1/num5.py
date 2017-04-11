'''
lab01 - 12.jpg  (Вариант 23)
'''

import math

b=0.3
x=5.2


t=(x*(b**2))+math.sqrt(x)
a=math.log10(math.fabs(t*x+(b**2)))
y=math.pow(math.log(1),(a+b))+((a**2)/a+t)      
print("y = "+str(y))
