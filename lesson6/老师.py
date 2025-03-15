# import pandas as pd
# import os
#
# path_list = os.listdir("./")
# path_list = [x for x in path_list if x.split(".")[-1] == "csv"]
# data = []
# for x in path_list:
#     pd_data = pd.read_csv(x, encoding="gbk")
#     data.append(pd_data[pd_data["ACCOUNT"].str.contains("李")])
# pd.concat(data).to_csv("new.csv")

# nums = [0, 1, 0, 3, 12]
# for x in nums:
#     if x == 0:
#         nums.remove(x)
#         nums.append(0)
# print(nums)


# 两个数组去重
# 找到小数组和大数组
# 循环小数组
# 判断小数组中的每一个值有没有在大数组中
# 判断没有，什么都不做，判断有，就加进新数组
# 输出答案
# n1 = [1, 2, 2, 3, 1]
# n2 = [2, 2, 3]
# n1 = list(set(n1))
# n2 = list(set(n2))
# max = n2 if len(n1) < len(n2) else n1
# min = n2 if len(n1) > len(n2) else n1
# data = []
# for x in min:
#     if x in max:
#         data.append(x)
# print(data)

# 循环父字符串
# 用s字符串的第一个去t字符串里面找
# 一旦找到，代表找到了第一个
# s字符串加一位，继续往t字符串后面找
# 又找到了，s字符串再加一位
# 判断s加了多少位 等于 len（s）的时候，是不是就代表s字符串全部找到了

# 3、给定字符串 s 和 t ，判断 s 是否为 t 的子序列。字符串的一个
# 子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符
# 相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，
# 而"aec"不是）。
#     输入：s = "abc", t = "ahbgdc"
#     输出：true
#     输入：s = "axc", t = "ahbgdc"
#     输出：false

# s = "abc"
# t = "ahbagdc"
# i = 0
# for x in t:
#     if s[i] == x:
#         i += 1
# print(i == len(s))


"""
4、写一个程序，输出从 1 到 n 数字的字符串表示。
    1. 如果 n 是3的倍数，输出“Fizz”；
    2. 如果 n 是5的倍数，输出“Buzz”；
    3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”

    n = 15,
    返回:
    [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]

5、在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。

    输入: "UD"
    输出: true
    解释：机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。

6、给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
    输入: [2,2,1]
    输出: 1

"""