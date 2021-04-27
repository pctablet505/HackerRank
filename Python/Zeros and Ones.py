import numpy as np

dimension = tuple(map(int, input().split()))
print(np.zeros(dimension, dtype=np.int))
print(np.ones(dimension, dtype=np.int))
