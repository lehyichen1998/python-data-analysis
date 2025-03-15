"""

# n = int(input('请输入一个号码: '))
#
# for x in range(n+1):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)

n = int(input()) + 1

for x in range(1, n):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
"""

"""
x, y = 0, 0
n = input('Enter: ')
for i in n:
    if i == "U":  # up y+1
        y += 1
    elif i == "D":  # down y-1
        y -= 1
    elif i == "R":  # right x+1
        x += 1
    elif i == "L":  # right x-1
        x -= 1

print((x == 0) and (y == 0))
"""

"""
s = [2, 2, 1, 1, 3]
for i in set(s):
    if s.count(i) == 1:
        print(i)

"""
