# -*- coding: utf-8 -*-
# 整数の入力
L = input().split()
N, X, T = [int(i) for i in L]

if N % X == 0:
    print(T * (N // X))
else:
    print(T * (N // X + 1))
