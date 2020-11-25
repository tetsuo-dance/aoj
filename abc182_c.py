import itertools
N = [int(i) for i in list(input())]
k = len(N)
ans = -1

for i in range(k):
    comb = list(itertools.combinations(N, k - i))
    t = list(map(sum, comb))
    t2 = [j % 3 for j in t]
    if 0 in t2:
        ans = i
        break

print(ans)
