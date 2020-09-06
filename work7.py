# -*- coding: utf-8 -*-
# 整数の入力
S = input()
T = input()

S_len = len(S)
T_len = len(T)
diff_len = S_len - T_len
tmp_count = 0
mached = 100000

for i in range(diff_len + 1):
    for j in range(T_len):
        if T[j] != S[j + i]:
            tmp_count = tmp_count + 1
    if tmp_count < mached:
        mached = tmp_count
    tmp_count = 0

print(mached)
