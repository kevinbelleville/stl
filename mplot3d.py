import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z
x = r * np.sin(theta)
y = r * np.cos(theta)



ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()