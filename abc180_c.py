N = int(input())
a = 1
ans = set()
while True:
    if a * a > N:
        break
    if N % a == 0:
        ans.add(a)
        ans.add(N // a)
    a += 1

ans = sorted(ans)
for i in range(len(ans)):
    print(ans[i])
