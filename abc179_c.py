N = int(input())
count = 0
tmp_count = 0

for c in range(1, N):
    for b in range(1, N):
        a, a_mod = divmod(N - c, b)
        if a_mod == 0:
            tmp_count += 1
        if a < b:
            if tmp_count != 1:
                tmp_count = (tmp_count - 1) * 2
            count += tmp_count
            tmp_count = 0
            break
print(count)
