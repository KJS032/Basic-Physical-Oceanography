import numpy as np
from sklearn.datasets import load_iris
X = load_iris().data
N=X.shape[0]
one = np.ones((N,1))
x = (X.T @ one) / N
print(one @ x.T)
