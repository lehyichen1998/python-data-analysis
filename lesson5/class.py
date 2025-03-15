import pandas as pd

pd_data = pd.read_table("疫情数据.csv", sep=",", encoding="gbk")
pd_data.dropna(how="all", inplace=True)
pd_data.新增 = pd_data.新增.fillna(222)
pd_data.loc[pd_data.新增 >= 50000, "严重程度"] = "非常严重"
pd_data.loc[(pd_data.新增 >= 30000) & (pd_data.新增 < 50000), "严重程度"] = "比较严重"
pd_data.loc[(pd_data.新增 >= 10000) & (pd_data.新增 < 30000), "严重程度"] = "一般严重"
pd_data.loc[(pd_data.新增 >= 1000) & (pd_data.新增 < 10000), "严重程度"] = "稍微严重"
pd_data.loc[(pd_data.新增 >= 0) & (pd_data.新增 < 1000), "严重程度"] = "一丢丢严重"

pd_data["总和"] = pd_data.新增 + pd_data.累计
title = pd_data.columns
data = ["长沙", 123, 23, 1, 0, "一丢丢严重"]
data = dict(zip(title, data))
new = pd.DataFrame(data, index=[len(pd_data)])
pd_data = pd_data.append(new)
pd_data.loc[pd_data.地区 == "长沙", "新增":"治愈"] = 332
pd_data.drop(pd_data[pd_data.死亡.isna() == True].index, inplace=True)
pd_data = pd_data.drop_duplicates("死亡", keep="last")
# pd_data = pd_data.drop_duplicates("死亡")
# pd_data.死亡 = pd_data.死亡.drop_duplicates()
# pd_data.死亡 = pd_data.死亡.drop_duplicates(keep="last")
# pd_data.to_csv("new.csv")
mean = pd_data.新增.mean()
std = pd_data.新增.std()
min = mean - (2 * std)
max = mean + (2 * std)
pd_data = pd_data.loc[(pd_data.新增 >= min) & (pd_data.新增 <= max), :]
pd_data.to_csv("error.csv")