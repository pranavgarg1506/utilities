import stats_test

a1 = [1,2,3,4,50]
b1 = [12,67,12,12,12]


import numpy as np

# Generate two lists with different variances
np.random.seed(42)  # For reproducibility

# List 1: Normally distributed with mean=10 and variance=4
a1 = np.random.normal(loc=10, scale=2, size=100)

# List 2: Normally distributed with mean=10 and variance=8
b1 = np.random.normal(loc=10, scale=4, size=100)
stats_test.CheckStats(a1,b1)