import numpy as np

P = np.array([100, 80, 50])
N = np.array([3, 4, 5])
total = (P @ N)

print(f"총 매수 금액: {total}만원")
