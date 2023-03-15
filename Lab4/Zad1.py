import pyswarms as ps
import numpy as np
import math
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt


def endurance(list):
    for solution in list:
        return -(math.exp(
                -2 * (solution[1] - math.sin(solution[0]))**2) + 
                math.sin(solution[2]*solution[4]) + math.cos(solution[3]*solution[5])
        )

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, 
options=options, bounds=my_bounds)
optimizer.optimize(endurance, iters=1000)

cost_history = optimizer.cost_history

plot_cost_history(cost_history)
plt.show()