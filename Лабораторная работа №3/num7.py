'''
lab3.4 - 13.jpg  (Вариант 23)
'''

import math
import pylab
from matplotlib import mlab 



xmin = 1
xmax = 3

dx=0.2

xlist=mlab.frange(xmin, xmax, dx)
ylist=[(math.log(x**2)-(1.8*math.sin(x))) for x in xlist]

pylab.plot (xlist, ylist)

pylab.show()


