import operator
import numpy as np


def create_data_set():
    group = [[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]
    label = ['A', 'A', 'B', 'B']
    return group, label
