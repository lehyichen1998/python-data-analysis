import pandas as pd
#  read_table 可以读取很多不同类型文件 不止csv还有txt
# pd_data = pd.read_table("coach.txt", sep=",", encoding="gbk", header=None)
# print(pd_data)
# 相对路径 ../day1
# 绝对路径 C:\Users\Administrator\PycharmProjects\shu_day1
pd_data = pd.read_csv("疫情数据.csv", encoding="gbk")
# del pd_data["死亡"]
# pd_data.to_csv("new.csv")



#  有没有一种好的办法去知道文件编码格式
import chardet
"""
    w : 写 但是如果重复写，那么会删除之前写的内容
    w+ ： 写 追加，如果没有文件则创建，如果有，那么追加到已有的文件中
    r：读
    b: 以二进制的形式
"""
# with open("疫情数据.csv", "rb") as f:
#     tem = chardet.detect(f.read())
#     print(tem)
#
# pd_data = pd.read_excel("userInfo.xlsx")
# del pd_data["Unnamed: 0"]
# print(pd_data.ACCOUNT.str.contains("李"))

# print(pd_data.values)
# print(pd_data.index)
# print(pd_data.columns)
# print(pd_data.dtypes)
# print(pd_data.size)
# print(pd_data.shape)
# print(pd_data)
# print()
# print(pd_data.T)

# print(pd_data.loc[1: 3, 'USER_ID':'sex'])
# print(pd_data.iloc[1:3, 0:3])

# pd_data.sort_values("治愈", inplace=True, ascending=False)
# print(pd_data.to_excel("zy.xlsx"))

import os
root = "ttest"
path_list = os.listdir(root)
d = []
for file_path in path_list:
    data = pd.read_csv(root + "/" + file_path, encoding="gbk")
    d.append(data[data.ACCOUNT.str.contains('李')])

pd.concat(d).to_csv("zong.csv")