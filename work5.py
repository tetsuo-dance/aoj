# -*- coding: utf-8 -*-
# 整数の入力
N = input()
tmp_list = list(map(int, input().split()))
A = tmp_list
count = 0
while True:
    max_value = max(tmp_list)
    now_ind = tmp_list.index(max_value)
    A[now_ind:len(tmp_list)] = list(map(lambda x: max_value - x, tmp_list[now_ind:len(tmp_list)]))
    #count = count + sum(list(map(lambda x: max_value - x, tmp_list[now_ind:len(tmp_list)])))
    tmp_list = tmp_list[0:now_ind]
    if now_ind == 0:
        break
print(sum(A))