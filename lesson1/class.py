import numpy as np

#
# py_data = [1, 2, 3]
# print(py_data * 3)
# np_data = np.array(py_data)
# print(np_data * 3)

# np_data = np.linspace(2, 3, 5)
# print(np_data)

# np_data = np.logspace(2, 3, 5, dtype="int64")
# print(np_data)

# list = list(range(1, 5))
# print(list)

# np_data = np.arange(1, 6)
# print(np_data)

# np_data = np.eye(5, dtype="int64")
# print(np_data)

# np_data = np.ones((3,5),dtype="int64")
# print(np_data)

# np_data = np.zeros((3, 5), dtype="int64")
# print(np_data)

# np_data=np.diag([1,2,3,4])
# print(np_data.shape)

# np_data = np.ones((2,3),dtype="int64")
# print(np_data.shape)
# print("row: "+ str(np_data.shape[0]))
# print("column: "+ str(np_data.shape[1]))

# np_data = np.zeros((2, 3))
# print(np_data)
# # print(np_data.size)
# # print(np_data.shape)
# np_data = np_data.reshape((3, 2))
# print(np_data)

# np_data = [[1, 2, 3, 4], [5, 6, 7, 8], [2, 3, 4, 5], [7, 7, 8, 8], [9, 9, 9, 9]]
# np_data = np.array(np_data)
# print(np_data)
# print()
# # print(np_data[1:])
# # print()
# # for x in range(1, 5):
# #     print(np_data[x])
# print(np_data[[2,4],[0]])

# np_data = np.zeros((3, 3), dtype="int64")
# np_data[0][0] = 1
# np_data[1][1] = 1
# np_data[2][2] = 1
# print(np_data)

np_data = np.zeros((4, 4), dtype="int64")
row = np_data.shape[0]
for x in range(4, row):
    np_data[x][x] = 1
