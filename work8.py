# -*- coding: utf-8 -*-
# 整数の入力
import itertools
from operator import add
from functools import reduce
N = int(input())
L = input().split()
LS = [int(i) for i in L]
count = 0
itr = list(itertools.combinations(LS, 2))
data = list(map(lambda x: (x[0] * x[1]) % 1000000007, itr))
ans = sum(data) % 1000000007
print(ans)