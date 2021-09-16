import numpy as np

st_matrix = []

def get_prob(state, time):
    initial = [1, 0]
    current = 1
    base = st_matrix
    while current < time:
        base = np.matmul(base,st_matrix)
        current += 1
    return np.matmul(initial, base)[state-1]
