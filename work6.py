# -*- coding: utf-8 -*-
# 整数の入力
L = input().split()
D, T, S = [int(i) for i in L]

if T*S < D:
    print("No")
else:
    print("Yes")

