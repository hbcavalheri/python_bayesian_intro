import numpy as np
import pymc as pm
import matplotlib.pyplot as plt

np.random.seed(42)
n_samples = 100
X = np.linspace(0, 10, n_samples)
true_slope = 2.5
true_intercept = 1.0
noise = np.random.normal(scale=1.0, size=n_samples)
y = true_slope * X + true_intercept + noise