#while True:
#    num_str = input().split()
#    n, x = [int(i) for i in num_str]
#    count = 0
#    if n == 0 and x == 0:
#        break
#    for i in range(1, n - 1):
#        for j in range(i + 1, n):
#            for k in range(j + 1, n + 1):
#                if i + j + k == x:
#                    count += 1    
#    print(count)

while True:
    num_str = input().split()
    n, x = [int(i) for i in num_str]
    count = 0
    if n == 0 and x == 0:
        break
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if j + 1 <= x - i - j <= n:
                count += 1
    print(count)