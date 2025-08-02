import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe

v = np.random.normal(size=100)
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)
print(res)

res1 = kstest(v, "norm")
print(res1)

res2 = describe(v)
print(res2)