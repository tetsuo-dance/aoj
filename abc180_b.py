import math
N = int(input())
tmp_str = input().split()
x = [int(i) for i in tmp_str]

m = 0
e = 0.0
c = 0

for i in range(N):
    m += abs(x[i])
    e += abs(x[i]) ** 2
    if abs(x[i]) > c:
        c = abs(x[i])

e = math.sqrt(e)

print(m)
print(e)
print(c)
