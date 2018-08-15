#This program admits the generation and visulatization of random walks on
#triangular, square, hexagonal, and diamond grids.
import matplotlib.pyplot as plt
import numpy as np
import random as random

numsteps = 1000
current_point = [0,0]
path = [[current_point[0]],[current_point[1]]]

triangular = np.array([[-np.sqrt(3)/2 , -0.5], [0,1.0], [np.sqrt(3)/2 , -0.5]])

hexagonal = np.array([[0, -1, -np.sqrt(3)/2, -0.5],
                       [0, -1 , np.sqrt(3)/2, -0.5],
                       [np.sqrt(3)/2, 0.5, 0, 1],
                       [np.sqrt(3)/2, 0.5, np.sqrt(3)/2, -0.5],
                       [-np.sqrt(3)/2, 0.5, -np.sqrt(3)/2, -0.5],
                       [-np.sqrt(3)/2, 0.5, 0, 1]])

diamond = np.array([[1,-1],[-1,-1],[1,1],[-1,1]])

vertical = np.array([[1,-1],[1,1]])

square = np.array([[0,-1],[1,0],[0,1],[-1,0]])


direction_dict = {"hexagonal":hexagonal, "triangular":triangular, "diamond":diamond,
                  "vertical":vertical, "square":square}

grid = "hexagonal"

for step in range(numsteps):
    if grid != "hexagonal":
        direction = random.choice(direction_dict[grid])
        current_point += direction
        path[0].append(current_point[0])
        path[1].append(current_point[1])

    if grid == "hexagonal":
        two_steps = random.choice(hexagonal)
        current_point += two_steps[0:2]
        path[0].append(current_point[0])
        path[1].append(current_point[1])

        current_point += two_steps[2:]
        path[0].append(current_point[0])
        path[1].append(current_point[1])

plt.plot(path[0],path[1])
plt.show()
