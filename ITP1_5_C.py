while True:
    num_str = input().split()
    H, W = [int(i) for i in num_str]
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            if i % 2 == 0:
                if j % 2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if j % 2 == 0:
                    print(".", end="")
                else:
                    print("#", end="")
        print()
    print()
