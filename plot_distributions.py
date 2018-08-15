import matplotlib.pyplot as plt
import numpy as np

def nCr(n,r):
    if r < 0:
        return 1
    if r > n:
        return 0
    return np.math.factorial(n) / (np.math.factorial(r) * np.math.factorial(n-r) )

#lam = lambda
def plot_poisson(lam, max_events):
    n_events = np.linspace(0,max_events,max_events+1)
    probabilities = np.array([])
    for i in n_events:
        probabilities = np.append(probabilities, (lam ** i) * (np.e ** -lam) / np.math.factorial(i) )
    #print("Error: " + str(1 - sum(probabilities)))
    plt.plot(n_events, probabilities)
    plt.xlabel("x")
    plt.title("Poisson Distribution with $\lambda$ = %s" %lam)
    plt.ylabel("P(X=x)")
    plt.show()

#p represents the probability of each Bernoulli trial
def plot_binomial(p, num_trials):
    n_events = np.linspace(0,num_trials,num_trials+1)
    probabilities = np.array([])
    for i in n_events:
        probabilities = np.append(probabilities, nCr(num_trials, i) * p ** i * (1.0-p)**(num_trials-i))
    plt.plot(n_events, probabilities)
    plt.xlabel("x")
    plt.title("Binomial Distribution p = %s, %s trials" %(p,num_trials))
    plt.ylabel("P(X=x)")
    plt.show()

#plots geometic distribution where each trial has a probability of success p
def plot_geometric(p, max_trials):
    n_events = np.linspace(0,max_trials, max_trials+1)
    probabilities = np.array([])
    for i in n_events:
        probabilities = np.append(probabilities, p ** i * (1.0-p))
    plt.scatter(n_events, probabilities)
    plt.title("Geometric Distribution p = %s" %p)
    plt.xlabel("x")
    plt.ylabel("P(X=x)")
    plt.show()

#num_stdev controls the amount of standard deviations to plot
def plot_normal(stdev, mean, num_stdev):
    n_events = np.linspace(mean-num_stdev*stdev,mean+num_stdev*stdev, 1000)
    probabilities = np.array([])
    for i in n_events:
        probabilities = np.append(probabilities, (2*np.pi*stdev**2)**-0.5 * np.e ** -(i-mean)**2 / (2*stdev**2))
    plt.plot(n_events, probabilities)
    plt.xlabel("x")
    plt.title("Normal Distribution $\mu$ = %s, $\\sigma$ = %s " %(mean, stdev))
    plt.ylabel("P(X=x)")
    plt.show()

#EXAMPLES
#plot_poisson(10, 20)
#plot_binomial(0.5, 1000)
plot_normal(1,0,3)
#plot_geometric(0.25,5)
