while True:
    val = input().split()
    s = [int(n) for n in val]
    s.sort()
    if s[0] == 0 and s[1] == 0:
        break
    print("{0} {1}".format(s[0], s[1]))
