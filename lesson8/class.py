import numpy as np
import matplotlib.pyplot as plt
import pylab as mpl

"""
incomplete
mpl.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(12, 8))
x = ["星期一", "星期二", "星期三", "星期四", "星期五"]
y = np.arange(0, 5)
y2 = np.arange(2, 7)
data = np.append(y, y2)
data = np.sort(data)
yaxis = list(set(data))
# yaxis = list(set(np.append(y, y2).sort()))
plt.plot(x, y, "--g", label="数据1", lw=2)
plt.plot(x, y2, "--r", label="数据2", lw=2)
plt.xlabel("日期")
plt.ylabel(np.arange(min([min(y), min(y2)]), max([max(y), max(y2)])), "数据")
plt.xticks(rotation=45)
plt.title("老师的图")
plt.grid(True, color="r", alpha=0.1)
plt.legend()
# plt.legend(loc="upper right")
plt.show()
"""

"""
mpl.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(12, 8))
date = ["9-1", "9-2", "9-3", "9-4", "9-5"]
zg = np.random.randint(0, 100, 5)
rb = np.random.randint(0, 100, 5)
mg = np.random.randint(0, 100, 5)
y = np.arange(min([np.min(zg), np.min(rb), np.min(mg)]), max([np.max(zg), np.max(rb), np.max(mg)])+10,10)

plt.plot(date, zg, "r", label="中国")
plt.plot(date, rb, "g", label="日本")
plt.plot(date, mg, "y", label="美国")
plt.grid(True, color="r", alpha=0.1)
plt.title("疫情数据")
plt.legend()
plt.xticks(rotation=-45)
plt.yticks(y)
plt.xlabel("日期")
plt.ylabel("死亡人数")
plt.show()
"""

data = np.arange(0, 5)
labels = ['Tom', 'Dick', 'Hanry', 'Sim', 'Jim']
plt.bar(range(len(data)), data, color="rgby", tick_label=labels)
plt.show()
