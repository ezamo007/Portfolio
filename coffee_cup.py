#Suppose there was a coffee machine that pours X cups of coffee at the push of a button
#Let X be a uniformly distributed random variable between 0 and 1.
#This program shows that, on average, it takes e (approx 2.718) presses to obtain at least 1 full cup.
import numpy as np
np.random.seed(10)

experiment_results = []
num_trials = 100000

for i in range(num_trials):
    coffee_volume = 0
    presses = 0
    while coffee_volume < 1:
        presses += 1
        coffee_volume += np.random.random()
    experiment_results.append(presses)

print(np.mean(experiment_results))
