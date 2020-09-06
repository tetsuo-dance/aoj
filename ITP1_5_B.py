while True:
    num_str = input().split()
    H, W = [int(i) for i in num_str]
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            print("#", end="")
        print()
    print()
