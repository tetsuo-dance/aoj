N = int(input())
tmp_str = input().split()
A = [int(i) for i in tmp_str]
gcd = 0
count = 0
ans = 0


for i in range(2, 1001):
    for j in range(len(A)):
        if A[j] % i == 0:
            count += 1
    if gcd <= count:
        gcd = count
        ans = i
    count = 0

print(ans)
