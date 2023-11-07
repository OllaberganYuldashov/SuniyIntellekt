import numpy as np

X = np.array([
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0]
])

w = np.array([[np.random.random() for j in range(3)] for i in range(4)])


# print(w)

def dist(x1, x2):
    s = 0
    for i in range(len(x1)):
        s += (x1[i] - x2[i]) ** 2
    return s


alfa = 0.3
predict = [0] * 8


for j in range(10000):
    i = 0
    for x in X:
        d1 = dist(x, w[:, 0])
        d2 = dist(x, w[:, 1])
        d3 = dist(x, w[:, 2])

        _min = min(d1, d2, d3)

        if _min == d1:
            # 1-class yaqin
            w[:, 0] = w[:, 0] + alfa * (x - w[:, 0])
            predict[i] = 0
        elif _min == d2:
            w[:, 1] = w[:, 1] + alfa * (x - w[:, 1])
            predict[i] = 1
        elif _min == d3:
            w[:, 2] = w[:, 2] + alfa * (x - w[:, 2])
            predict[i] = -1
        i += 1

predict = np.array(predict)
print(predict)