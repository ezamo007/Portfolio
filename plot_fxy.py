#This program plots two variable functions. More negative values appear more red,
#and positive values appear green

import numpy as np
import matplotlib.pyplot as plt

domain = [-2*np.pi,2*np.pi,-2*np.pi,2*np.pi] #[x_min, x_max, y_min, y_max]
#Finer resolution results in longer computation time but a smoother image.
resolution = 0.5

x_array = np.linspace(domain[0],domain[1], (domain[1]-domain[0])/resolution)
y_array = np.linspace(domain[2],domain[3], (domain[3]-domain[2])/resolution)

#f is the function the program attempts to plot
def f(coords):
    x = coords[0]
    y = coords[1]
    return 50 * np.cos(x-2*y)

for x_point in x_array[:-1]:
    for y_point in y_array[:-1]:
        smushed_value = 1 / (1 + np.e**(-0.5 * f([x_point, y_point])))
        plt.arrow(x_point,y_point, 1,0, width= resolution, head_width = 0, color = (1-smushed_value, smushed_value,0) )

plt.axis(domain)
plt.show()
