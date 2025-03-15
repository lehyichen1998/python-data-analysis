"""
using visual studio code
learn html
"""

import numpy as np
# 解决matplotlib中文乱码问题
import pylab as mpl
# reshape (12, 13)
import matplotlib.pyplot as plt
# 指定matplotlib的文字格式，matplotlib默认不支持中文字体
# 所以咱们要手动指定
# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# # 通过figure里面的figsize属性设置画布大小
# plt.figure(figsize=(12, 8))
# # 设置x轴的刻度文本
# x = ["星期一", "星期二", "星期三", "星期四", "星期五"]
# # 根据x轴长度，自动生成y轴数据
# y = np.arange(0, 5)
# y2 = np.arange(2, 7)
# # 合并两个数组
# data = np.append(y, y2)
# # 对合并数据进行排序
# data = np.sort(data)
# # 对合并数据进行去重
# yaxis = list(set(data))
# # 得到合并之后的排序数据
# # 在画布上绘制一条线，并且这条线必须x和y的数据对应起来
# # label属性给这条线取名字, --g代表虚线且绿色
# plt.plot(x, y, '--g', label="数据1", lw=2)
# plt.plot(x, y2, '--r', label="数据2", lw=2)
# # 设置x轴的标题
# plt.xlabel("日期")
# # 设置y轴标题
# plt.ylabel("数据")
# # 设置x轴样式
# plt.xticks(rotation=45)
# # 设置y轴样式
# plt.yticks(yaxis)
# # 设置整个图的标题
# plt.title("老师的图")
# # 打开标尺 red green
# plt.grid(True, color="r", alpha=0.1)
# # 打开图例
# plt.legend()
# 展示图例

# y 死亡人数
# x 最近十天的日期
# 红色线代表中国， 绿色线代表日本， 黄色代表美国
# 建议大家用np里面的随机数组
# 标尺，图例，y轴不得打乱，x轴刻度旋转-45度
# np_data = np.random.randint(0, 3, size=7)
# print(np_data)
# 日期
# date = ["9-1", "9-2", "9-3", "9-4", "9-5"]
# # 中国死亡人数
# zg = np.random.randint(0, 100, 5)
# # 日本
# rb = np.random.randint(0, 100, 5)
# # 美国
# mg = np.random.randint(0, 100, 5)
# y = np.arange(0, max([np.max(zg), np.max(rb), np.max(mg)])+10, 10)
#
# # 所以咱们要手动指定
# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# # 通过figure里面的figsize属性设置画布大小
# plt.figure(figsize=(12, 8))
# plt.plot(date, zg, "r", label="中国")
# plt.plot(date, rb, "g", label="日本")
# plt.plot(date, mg, "y", label="美国")
# plt.grid(True, color="r", alpha=0.1)
# plt.title("疫情数据")
# plt.legend()
# plt.xticks(rotation=-45)
# plt.yticks(y)
# plt.xlabel("日期")
# plt.ylabel("死亡人数")
# plt.show()

# 柱状图
data = np.arange(0, 5)
labels = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
plt.bar(range(len(data)), data, color=['r', 'g', 'b', 'y'], tick_label=labels)
plt.show()