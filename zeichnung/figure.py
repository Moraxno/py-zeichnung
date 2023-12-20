from matplotlib.figure import FigureBase
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.interactive(True)

@np.vectorize
def inch2cm(val_in: float):
    return val_in * 2.54

@np.vectorize
def cm2inch(val_cm: float):
    return val_cm / 2.54

UNIT_VEC2D_X = np.array([1, 0])
UNIT_VEC2D_Y = np.array([0, 1])

def angle_of_vector(vector: np.array) -> float:
    vec_len = np.linalg.norm(vector)

    if vec_len <= 0:
        return np.nan
    
    return np.arccos(np.dot(UNIT_VEC2D_X, vector) / vec_len)


def add_dimension(figure: FigureBase, start_point: (float, float), end_point: (float, float), offset: float, label: str):
    pass