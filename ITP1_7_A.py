while True:
    num_str = input().split()
    m, f, r = [int(i) for i in num_str]
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        print("F")
    elif m + f >= 80:
        print("A")
    elif 65 <= m + f < 80:
        print("B")
    elif 50 <= m + f < 65:
        print("C")
    elif 30 <= m + f < 50:
        if r < 50:
            print("D")
        else:
            print("C")
    else:
        print("F")
