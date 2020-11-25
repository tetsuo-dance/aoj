num_str = input().split()
n, m, l = [int(i) for i in num_str]

A = [input().split() for i in range(n)]
B = [input().split() for i in range(m)]

sum = 0

for i in range(n):
    for j in range(l):
        for k in range(m):
            sum += int(A[i][k]) * int(B[k][j])
        print(sum, end="")
        sum = 0
        if j != l - 1:
            print(" ", end="")
    print()
