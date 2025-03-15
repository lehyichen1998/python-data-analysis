import numpy as np

# np_data = np.arange(0,10)
# print(np_data)
# print(np_data.reshape(2,5))

# l=[1,2,2,4,4,5]
# np_data=np.array(l)
# # print(list(set(np_data)))
# np_data = np.unique(np_data)
# print(np_data)

# ===========================================================================
# lst = [1, 2, 3, 4, 5, 6]
# l = [1, 2, 3, 4, 5]

# np_data = np.arange(1, 7)
# len = np_data.size
# result = 0
# if len % 2 == 0:
#     d = int(len / 2)
#     result = (np_data[d] + np_data[d - 1]) / 2
# else:
#     d = int(len / 2)
#     result = np_data[d]
# print(result)
# ==============================================================================
# s = "abcba"
# p = s[::-1]
# if s == p:
#     print(f"{s}是一个回文")
# else:
#     print(s + "不是一个回文")
# ===============================================================================
# n = int(input("请输入: "))
# for x in range(2, n + 1):
#     for y in range(2, int(x / 2 + 1)):
#         if x % y == 0:
#             break
#     else:
#         print(x)
# ===============================================================================
n = int(input("请输入: "))
# for x in range(1, n + 1):
#     for y in range(0,x):
#         print(1,end=" ")
#     print()
data = []
for x in range(n):
    row = []
    for y in range(0, x+1):
        try:
            row.append(data[x - 1][y] + data[x - 1][y - 1])
        except:
            row.append(1)
    row[0] = 1
    data.append(row)

for x in data:
    for y in x:
        print(y,end=" ")
    print()
