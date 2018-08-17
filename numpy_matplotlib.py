import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,3,31)
y1 = x**2
y2 = 25-x**3
plt.plot(x,y1,'bo-') # blå, heltrukket linje, sirkel for hvert av punktene
plt.plot(x,y2,'r--') # rød, stiplet linje
plt.show()