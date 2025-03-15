import numpy as np
lst = [1, 2, 3, 4, 5, 6]
l = [1, 2, 3, 4, 5]

np_data = np.arange(1, 7)
len = np_data.size
result = 0
if len % 2 == 0:
    d = int(len / 2)
    result = (np_data[d] + np_data[d - 1]) / 2
else:
    d = int(len / 2)
    result = np_data[d]
print(result)