import pytest
from zeichnung.figure import angle_of_vector

import numpy as np

@pytest.mark.parametrize("vector,angle", [
    (np.array([ 1,  0]),         0    ),
    (np.array([ 5,  0]),         0    ),
    (np.array([-1,  0]),         np.pi),
    (np.array([-5,  0]),         np.pi),
    (np.array([ 0,  1]), 1 / 2 * np.pi),
    (np.array([ 0,  5]), 1 / 2 * np.pi),
    (np.array([ 0, -1]), 1 / 2 * np.pi),
    (np.array([ 0, -5]), 1 / 2 * np.pi),
    (np.array([-1, -1]), 3 / 4 * np.pi),
    (np.array([-5, -5]), 3 / 4 * np.pi),
])
def test_angle_of_vector(vector, angle):
    assert angle_of_vector(vector) == pytest.approx(angle)

def test_angle_of_zero_vector_is_nan():
    assert np.isnan(angle_of_vector(np.array([0, 0])))