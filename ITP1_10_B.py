import math
my_str = input().split()
a, b, C = [float(i) for i in my_str]

cosC = math.cos(math.radians(C))

cc = math.sqrt(b ** 2 + a ** 2 - 2*b*a*cosC)

L = a + b + cc
S = (1 / 2) * a * b * math.sin(math.radians(C))
h = (2 * S) / a

print(S)
print(L)
print(h)
