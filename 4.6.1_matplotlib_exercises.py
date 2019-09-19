import matplotlib.pyplot as plt
import math
import random
import numpy as np 

x = list(range(150))
plt.plot(x)
plt.show()

plt.plot(x)
plt.xlim(-20, 200)
plt.ylim(-5, 160)
plt.show()

plt.plot(x, c='red')
plt.show()

from random import randint

# Some random data
x1 = [randint(-5, 25) + n for n in range(150)]
x2 = [x + randint(-6, 6) for x in x1]

# we can use the alpha kwarg to define how transparent the color is
plt.plot(x1, c='green', alpha=0.9)
plt.plot(x2, c='red', alpha=0.7)
plt.show()

# plotting our random data from the last step
plt.scatter(range(len(x1)), x1)
plt.scatter(range(len(x2)), x2)
plt.show()

# 1. Use matplotlib to plot the following equation.

x = range(-10, 10)
y = [i**2-i+2 for i in x]
plt.plot(x,y, c='blue')
plt.annotate('(0, 0)', xy=(0, 0), xytext=(2, 1),
             arrowprops={'facecolor': 'blue'})
plt.show()

# 2. Create and label 4 separate charts for the following 
# equations (choose a range for x that makes sense):

x = range(0, 10)
y = [i**.5 for i in x]
plt.plot(x,y, c='red')
plt.xlabel('$x$')
plt.ylabel('$\sqrt{x}$')
plt.show

x = range(0, 10)
y = [i**3 for i in x]
plt.plot(x,y, c='yellow')
plt.xlabel('$x$')
plt.ylabel('${x^3}$')
plt.show

x = np.arange(-10, 10, .1)
y = [math.tan(i) for i in x]
plt.plot(x,y, c='orange')
plt.ylim(-10,10)
plt.xlabel('$x$')
plt.ylabel('$tan({x})$')
plt.show

x = range(-10, 10)
y = [2**i for i in x]
plt.plot(x,y, c='purple')
plt.xlabel('$x$')
plt.ylabel('${2^x}$')
plt.show

# x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# plt.plot(x, np.tan(x))
# plt.ylim(-10, 10)
# plt.show()

# 3. Combine the figures you created in the last step into
# one large figure with 4 subplots.

plt.subplot(221)
x = range(0, 10)
y = [i**.5 for i in x]
plt.plot(x,y, c='red')
plt.show

plt.subplot(222)
x = range(0, 10)
y = [i**3 for i in x]
plt.plot(x,y, c='yellow')
plt.show

plt.subplot(223)
x = np.arange(-10, 10, .1)
y = [math.tan(i) for i in x]
plt.plot(x,y, c='orange')
plt.ylim(-10,10)
plt.show

plt.subplot(224)
x = range(-10, 10)
y = [2**i for i in x]
plt.plot(x,y, c='purple')
plt.show

# 4. Comine the figures you created in the last step into
# one figure where each of the 4 equations has a different
# color for the points. Be sure to include a legend.

plt.subplot(221)
x = range(-10, 10)
y1 = [i**.5 for i in x]
y2 = [i**3 for i in x]
y3 = [math.tan(i) for i in x]
y4 = [2**i for i in x]

plt.plot(x,y1, c='red', label='$\sqrt{x}$')
plt.plot(x,y2, c='yellow', label='${x^3}$')
plt.plot(x,y3, c='orange', label='$tan({x})$')
plt.plot(x,y4, c='purple', label='${2^x}$')

plt.ylim(-5,5)

plt.legend(loc='upper left', prop={'size': 4})
plt.title('wow')

plt.show

# Bonus

# Write the code necessary to write your name on a chart. Use box
# letters. Bonus: use curves for letters in your name that have
# curves in them.




