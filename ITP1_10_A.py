import math
my_str = input().split()
x1, y1, x2, y2 = [float(i) for i in my_str]

print(math.sqrt((x1-x2)**2 + (y1-y2) ** 2))
