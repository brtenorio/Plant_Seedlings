import pytest 
from plant_seedlings.evaluate_model import evaluate_model
from plant_seedlings.data_generator import test_generator

def test_model():
    eval = evaluate_model(test_generator)
    assert eval[1] > 0.75

