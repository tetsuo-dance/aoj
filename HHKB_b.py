tmp_str = input().split()
H, W = [int(i)for i in tmp_str]
count = 0
before_raw = "#"*W
for i in range(H):
    now_raw = input()
    for j in range(W - 1):
        if now_raw[j] == "." and now_raw[j + 1] == ".":
            count += 1
    for j in range(W):
        if now_raw[j] == "." and before_raw[j] == ".":
            count += 1
    before_raw = now_raw

print(count)
