import math

n = int(input())
x = input().split()
x_float = [float(i) for i in x]
y = input().split()
y_float = [float(i) for i in y]
d = 0


for p in range(1, 4):
    d = 0
    for i in range(n):
        d += (abs(x_float[i] - y_float[i]))**p
    d = d ** (1 / p)
    print(d)

inf_list = [abs(x - y) for (x, y) in zip(x_float, y_float)]

print(max(inf_list))
