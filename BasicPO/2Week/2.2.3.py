from sklearn.datasets import load_digits
X = load_digits().data
d1 = digits.images[0]
d2 = digits.images[9]
v1 = d1.reshape(64,1)
v2 = d2.reshape(64,1)
(v1.T @ v2)[0][0]

similarity = (X @ X.T)
or i in range(len(similarity)):
    similarity[i, i] = 0
for i in range(len(similarity)):
    for j in range(i + 1, len(similarity)):
        print(f"이미지 {i + 1}과 이미지 {j + 1}의 유사도: {similarity[i, j]}")
