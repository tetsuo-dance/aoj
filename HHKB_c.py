N = int(input())
tmp_str = input().split()
p = [int(i) for i in tmp_str]
nums = set()
minnum = 0
for i in range(N):
    nums.add(p[i])
    if p[i] == minnum:
        while minnum in nums:
            minnum += 1
    print(minnum)
