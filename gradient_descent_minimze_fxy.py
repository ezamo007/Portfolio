#This program uses a rudimentary gradient descent technique to find a local
#minimum of a function of two variables on a given domain.
import numpy as np
import matplotlib.pyplot as plt

#Example: x*(y-1)*np.sin(x*y) reaches a minimum of -0.240125 on [0,1] x [0,1] at (1, 0.479731)
domain = [-2*np.pi,2*np.pi,-2*np.pi,2*np.pi] #[x_min, x_max, y_min, y_max]
test_coordinates = [0.0, 0.0]
RESOLUTION = 0.001
N_ITERATIONS = 10000
search_path = [[],[],[]]

#f is the function the program attempts to minimize
def f(coords):
    x = coords[0]
    y = coords[1]
    return np.cos(x)-np.sin(y)

#gradient returns a numpy array of magnitude RESOLUTION, in the
#direction of (an approximation of) the gradient of f at the given coordinates.
def gradient(coords):
    x = coords[0]
    y = coords[1]
    h = RESOLUTION
    grad = np.array([f((x+h, y)) - f((x,y)), f((x,y+h)) - f((x,y))])
    return h * grad / np.linalg.norm(grad)

for i in range(N_ITERATIONS):
    search_path[0].append(test_coordinates[0])
    search_path[1].append(test_coordinates[1])
    search_path[2].append(f(test_coordinates))

    if i%100 == 0:
        print(test_coordinates)
        print(f(test_coordinates))
        print("\n")

    if test_coordinates[0] < domain[0] or test_coordinates[0] > domain[1] or test_coordinates[1] < domain[2] or test_coordinates[1] > domain[3]:
        quit()
    else:
        test_coordinates -= gradient(test_coordinates)

dot_colors = []
for item in search_path[2]:
    if item <= 0: dot_colors.append('r')
    else: dot_colors.append('g')



plt.scatter(search_path[0], search_path[1], np.abs(search_path[2]), dot_colors)
plt.axis(domain)
plt.grid()
plt.show()
