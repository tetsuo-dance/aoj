S_str = input()
S = int(S_str)
eight_list = []
ans = "No"
count = 0

for i in range(100, 1000):
    if i % 8 == 0:
        eight_list.append(str(i))

if len(S_str) == 1:
    if S % 8 == 0:
        ans = "Yes"
elif len(S_str) == 2:
    s2 = S_str[1] + S_str[0]
    if S % 8 == 0 or int(s2) % 8 == 0:
        ans = "Yes"
else:
    for i in range(len(eight_list)):
        tmp_str = S_str
        for j in range(len(eight_list[i])):
            if eight_list[i][j] in tmp_str:
                tmp_str = tmp_str.replace(eight_list[i][j], "", 1)
                count += 1
        if count == len(eight_list[i]):
            ans = "Yes"
            break
        count = 0
print(ans)
