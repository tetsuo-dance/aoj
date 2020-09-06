n = int(input())
num_str = input().split()
A = [int(i) for i in num_str]
print(" ".join([str(i) for i in A]))

for i in range(1, len(A)):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = v
    print(" ".join([str(i) for i in A]))
