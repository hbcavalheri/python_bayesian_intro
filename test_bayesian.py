import numpy as np
import pytest
from bayesian import BayesianAnalysis

@pytest.fixture
def setup_data():
    """ Fixture para preparar os dados que serão usados nos testes. """
    np.random.seed(42)
    n_samples = 100
    X = np.linspace(0, 10, n_samples)
    true_slope = 2.5
    true_intercept = 1.0
    noise = np.random.normal(scale=1.0, size=n_samples)
    y = true_slope * X + true_intercept + noise
    return X, y

def test_build_model(setup_data):
    """ Testa se o modelo foi construído corretamente e o trace foi gerado. """
    X, y = setup_data
    model = BayesianAnalysis(X, y)
    model.build_model()

    assert model.model is not None, "O modelo não foi construído corretamente."
    assert model.get_trace() is not None, "O trace não foi gerado."

def test_trace_length(setup_data):
    """ Testa se o trace contém o número correto de amostras. """
    X, y = setup_data
    model = BayesianAnalysis(X, y)
    model.build_model()
    trace = model.get_trace()

    assert len(trace["slope"]) == 8000, "O número de amostras no trace está correto."

