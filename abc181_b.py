N = int(input())
sum = 0

for i in range(N):
    tmp_str = input().split()
    A, B = [int(i) for i in tmp_str]
    if A == 1 and A != B:
        sum += (B*(B + 1)) // 2
    elif A == B:
        sum += A
    else:
        sum += (B * (B + 1)) // 2 - ((A - 1) * ((A - 1) + 1)) // 2

print(sum)
