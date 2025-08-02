from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)
new_array = interp_func(np.arange(2.1, 3, 0.1))
print(new_array)

ys1 = xs**2 + np.sin(xs) + 1
interp_func1 = UnivariateSpline(xs, ys1)
new_array1 = interp_func1(np.arange(2.1, 3, 0.1))
print(new_array1)


interp_func2 = Rbf(xs, ys1)
new_array2 = interp_func2(np.arange(2.1, 3, 0.1))
print(new_array2)