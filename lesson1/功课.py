import numpy as np

np_data = np.zeros((3, 3), dtype="int64")
# np_data[0][2]=1
# np_data[1][1]=1
# np_data[2][0]=1

# row = np_data.shape[0]-1
# for x in range(0, 3):
#     np_data[x][row - x] = 1


for x in range(0, 3):
    np_data[x][x] = 1
    np_data[x] = np_data[x][::-1]
print(np_data)


# data=[1,2,3,4]
# print(data[::-1])