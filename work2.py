# -*- coding: utf-8 -*-
# 整数の入力
import itertools
N = int(input())
L = input().split()
LS = [int(i) for i in L]
count = 0
itr = list(itertools.combinations(LS, 3))

for s in itr:
    if s[0] + s[1] > s[2] and s[1] + s[2] > s[0] and s[2] + s[0] > s[1] \
        and s[0] != s[1] and s[1] != s[2] and s[2] != s[0]：
    count = count + 1
print(count)
