while True:
    trump_str = input()
    if trump_str == "-":
        break
    m = int(input())

    for i in range(m):
        h = int(input())
        sliced = trump_str[0:h]
        lefted = trump_str[h:len(trump_str) + 1]
        trump_str = lefted + sliced

    print(trump_str)
