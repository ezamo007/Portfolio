#This program provides a numerical solution to ordinary differential equations of the form
#y' = f(t,y) using the popular fourth-order Runge-Kutta method (RK4).
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

h = 0.01
t0 = 0
y0 = 2.25
num_steps = 500

def f(y, t):
    return np.cos(y*t-y)

def RK4_solve():
    t_array = np.array([t0])
    y_array = np.array([y0])

    for step in range(num_steps):
        y_k = y_array[-1]
        t_k = t_array[-1]
        k1 = h*f(y_k,t_k)
        k2 = h*f(y_k + k1*0.5, t_k + h*0.5)
        k3 = h*f(y_k + k2*0.5, t_k + h*0.5)
        k4 = h*f(y_k + k3, t_k + h)
        y_array = np.append(y_array, y_k + (k1 + k2 + k3 + k4)/6.0 )
        t_array = np.append(t_array, t_k + h)
    return t_array, y_array

t_array, y_array = RK4_solve()
plt.plot(t_array, y_array)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()
