import pandas as pd
import chardet
import os

"""
# pd_data=pd.read_table("疫情数据.csv",sep=",",encoding="gbk")
# print(pd_data["新增"])
# print(pd_data)
"""

"""
# pd_data=pd.read_table("coach(1).txt",sep=",",encoding="gbk")
pd_data = pd.read_table("coach(1).txt", sep=",", encoding="gbk", header=None)
print(pd_data)
"""
# 相对路径 ../../疫情数据.csv
# 绝对路径 D:\Online_Class\数据可视化\lesson4\疫情数据.csv
"""
pd_data = pd.read_csv("疫情数据.csv", encoding="gbk")
del pd_data["死亡"]
pd_data.to_csv("new疫情数据.csv")
print(pd_data)
"""

"""
pd_data = pd.read_excel("userInfo.xlsx",engine="openpyxl")
print(pd_data)
"""

"""
w: will overwrite if same
w+: will not overwrite if same
r: read data
b: 以二进制的形式
"""

"""
with open("疫情数据.csv", "rb") as f:
    tem = chardet.detect(f.read())
    print(tem)
"""

"""
pd_data = pd.read_excel("userInfo.xlsx", engine="openpyxl")
pd_data.drop(pd_data[pd_data.ACCOUNT.str.startswith("李")==True].index,inplace=True)
# pd_data.drop(pd_data.ACCOUNT.str.startswith("李").index)

pd_data.to_excel("newexcel.xlsx")
print(pd_data)

"""




"""
pd_data = pd.read_excel("userInfo.xlsx", engine="openpyxl")
# print(pd_data.values)
# print(pd_data.index)
# print(pd_data.columns)
# print(pd_data.dtypes)
# print(pd_data.size) # row X column
# print(pd_data.shape)
# print(pd_data.T)

# print(pd_data.loc[1:3, "USER_ID":"sex"])
# print(pd_data.iloc[1:3, 0:3])
"""

"""
pd_data = pd.read_table("疫情数据.csv", sep=",", encoding="gbk")
pd_data.sort_values("治愈", inplace=True,ascending=False)
pd_data.to_excel("zy.xlsx")
# pd_data.to_excel("D:\Online_Class\数据可视化\zy.xlsx")
print(pd_data)
"""

root = "ttest"
path_list = os.listdir(root)
d = []
for file_path in path_list:
    data = pd.read_csv(root + "/" + file_path, encoding="gbk")
    d.append(data[data.ACCOUNT.str.contains('李')])

pd.concat(d).to_csv("zong.csv")
