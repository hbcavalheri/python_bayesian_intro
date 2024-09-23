import numpy as np
import pymc as pm

class BayesianAnalysis:
    def __init__(self, X, y, true_slope=2.5, true_intercept=1.0, noise_scale=1.0):
        self.X = X
        self.y = y
        self.true_slope = true_slope
        self.true_intercept = true_intercept
        self.noise_scale = noise_scale
        self.model = None
        self.trace = None

    def build_model(self):
        with pm.Model() as self.model:
            slope = pm.Normal("slope", mu=0, sigma=10)
            intercept = pm.Normal("intercept", mu=0, sigma=10)
            sigma = pm.HalfNormal("sigma", sigma=1)

            mu = slope * self.X + intercept

            y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=self.y)
            self.trace = pm.sample(2000, return_inferencedata=False)

    def get_trace(self):
        return self.trace
