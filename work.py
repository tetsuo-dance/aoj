n = int(input())
for i in range(3, n + 1):
    x = i
    if x % 3 == 0 or x % 10 == 3:
        print(" " + str(i), end="")
    else:
        while True:
            x = x // 10
            if x == 0:
                break
            if x % 10 == 3:
                print(" " + str(i), end="")
                break
print()
