import pandas as pd
import os

"""
path_list = os.listdir("./")
path_list = [x for x in path_list if x.split(".")[-1] == "csv"]
data = []
for x in path_list:
    pd_data = pd.read_csv(x, encoding="gbk")
    data.append(pd_data[pd_data["ACCOUNT"].str.contains("李")])
pd.concat(data).to_csv("new.csv")
"""

"""
nums = [0, 1, 0, 3, 12]
for x in nums:
    if x == 0:
        nums.remove(x)
        nums.append(0)

print(nums)
"""

"""
nums1 = [1, 2, 2, 3, 1]
nums1 = set(nums1)
nums2 = [2, 2, 3]
nums2 = set(nums2)
data = []
max = nums2 if len(nums1) < len(nums2) else nums1
min = nums2 if len(nums1) > len(nums2) else nums1

for x in min:
    if x in max:
        data.append(x)
print(data)
"""

s = "abc"
t = "ahbagdc"
i = 0
for x in t:
    if s[i] == x:
        i += 1

print(i == len(s))

s = "axc"
t = "ahbagdc"
i = 0
for x in t:
    if s[i] == x:
        i += 1

print(i == len(s))
