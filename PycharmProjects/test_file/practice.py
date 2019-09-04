import numpy as np
import matplotlib.pyplot as plt


def get_map():
    x = np.arange(1, 2)
    y = x*2 + 1
    plt.xlabel('Years')
    plt.ylabel('Money')
    plt.plot(x, y)
    plt.show()


# get_map()


def get_max(data):
    n = len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


a = [2, 5, 2, 5, 7, 1, 0, 8, 9, 6]
res = get_max(a)
print(res)
