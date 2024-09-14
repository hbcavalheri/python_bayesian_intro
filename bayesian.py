import numpy as np
import pymc as pm

np.random.seed(42)
n_samples = 100
X = np.linspace(0, 10, n_samples)
true_slope = 2.5
true_intercept = 1.0
noise = np.random.normal(scale=1.0, size=n_samples)
y = true_slope * X + true_intercept + noise

with pm.Model() as model:
    slope = pm.Normal("slope", mu=0, sigma=10)
    intercept = pm.Normal("intercept", mu=0, sigma=10)
    sigma = pm.HalfNormal("sigma", sigma=1)

    mu = slope * X + intercept

    y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)

    trace = pm.sample(2000, return_inferencedata=False)