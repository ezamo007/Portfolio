#Plots a walk of numsteps steps of length 1 (or a random length between 0 and 1)
#where the direction of each step is randomly chosen.
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
numsteps = 100

current_point = [0,0]
path = [[current_point[0]],[current_point[1]]]

for i in range(numsteps):
    #Picks a random angle between 0 to 2pi radians.
    angle = 2*np.pi*np.random.random()

    #Step length can be set to 1 or a random number between 0 and 1.
    step_length = 1
    #step_length = np.random.random()

    #Converts from polar coordinates to carterian coordinates.
    direction = np.array([np.cos(angle), np.sin(angle)])
    current_point += direction * step_length
    path[0].append(current_point[0])
    path[1].append(current_point[1])

plt.plot(path[0],path[1], linewidth = 3)
plt.show()
