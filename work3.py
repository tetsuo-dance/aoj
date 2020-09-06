# -*- coding: utf-8 -*-
# 整数の入力
L = input().split()
LS = [int(i) for i in L]
X = abs(LS[0])
K = LS[1]
D = LS[2]

length = X % D
move = X // D

if X - K * D >= 0:
    print(X - K * D)
else:
    if (K - move) % 2 == 0:
        print(length)
    else:
        print(length + 1)
