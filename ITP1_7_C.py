num_str = input().split()
r, c = [int(i) for i in num_str]

c_sum = [0] * (c + 1)

for i in range(r):
    r_str_list = input().split()
    r_num_list = [int(i) for i in r_str_list]
    r_num_list.append(sum(r_num_list))
    for j in range(c + 1):
        c_sum[j] += r_num_list[j]
    r_str_list = [str(i) for i in r_num_list]
    print(" ".join(r_str_list))
c_sum_str = [str(i) for i in c_sum]
print(" ".join(c_sum_str))




