from scipy.optimize import minimize_scalar
from scipy.optimize import differential_evolution

def quadratic_function(x):
    return (x - 3) ** 2 + 5

def global_objective(x):
    return x[0] ** 2 + x[1] ** 2

result_minimize_scalar = minimize_scalar(quadratic_function)
print("Optimal Solution: ", result_minimize_scalar.x)
print("Minimum Value: ", result_minimize_scalar.fun)

result_differential_evolution = differential_evolution(global_objective, [(-2, 2), (-2, 2)])
print("Global Optimal Solution: ", result_differential_evolution.x)
print("Global Minimum Value: ", result_differential_evolution.fun)