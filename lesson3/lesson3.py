import numpy as np
import random

'''
# np_data1 = np.arange(0, 9)
# np_data2 = np.arange(5, 15)
# data = np.append(np_data1, np_data2)
# data = np.sort(data)
# size = data.size
# result = 0
# if size % 2 == 1:
#     result = data[int(size / 2)]
# else:
#     s = int(size / 2)
#     result = (data[s] + data[s - 1]) / 2
# print(result)
'''

"""
data = []
n = int(input())

for x in range(0, n):
    row = []
    for y in range(0, x + 1):
        if x - 1 <= 0:
            row.append(1)
        elif y - 1 < 0 or y >= len(data[x - 1]):
            row.append(1)
        else:
            row.append(data[x - 1][y] + data[x - 1][y - 1])
    data.append(row)

for x in data:
    for y in x:
        print(y,end=" ")
    print()
"""

"""
np_data = np.random.randint(0, 10)
print(np_data)
"""

"""
np_data = np.loadtxt("coach.txt", delimiter=',', dtype="str")
print(np_data)
print()
print(np_data[:, 4].argsort())
# asc
print()
print("ASC")
print(np_data[np_data[:, 4].argsort()])
#  desc
print()
print("DESC")
print(np_data[np_data[:, 4].argsort()[::-1]])
"""

"""
# def my_sort(data):
#     length = len(data)
#     for x in range(0, length):
#         for y in range(x + 1, length):
#             if data[x] < data[y]:
#                 t = data[x]
#                 data[x] = data[y]
#                 data[y] = t
#     return data

def my_sort(data, order=True):
    length = len(data)
    for x in range(0, length):
        num = x
        for y in range(x + 1, length):
            if order:
                if data[num] < data[y]:
                    num = y
            else:
                if data[num] > data[y]:
                    num = y
        if num != x:
            t = data[num]
            data[num] = data[x]
            data[x] = t

    return data


data = [4, 1, 3, 3, 1, 7]
print(my_sort(data, False))

"""

"""
n = int(input("Enter Number: "))
data = []
data.append(1)
data.append(1)
for x in range(2, n):
    data.append(data[x - 1] + data[x - 2])
print(data)
"""

"""
for x in range(100, 1000):
    bai = int(x / 100)
    shi = int(x / 10 % 10)
    ge = int(x % 10)
    if (bai ** 3 + shi ** 3 + ge ** 3) == x:
        print(x)
"""


def fun(n):
    if n <= 2:
        return 1
    return fun(n - 1) + fun(n - 2)


n = int(input("Enter Number: "))
print(fun(n))
