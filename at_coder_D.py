N = int(input())
s = []
for i in range(5):
    s.append(input())
num_count = [0] * N
counter = 0

for i in range(0, 5):
    for j in range(0, 4 * N, 4):
        num_count[counter] += s[i][j + 1:j + 4].count("#")
        counter += 1
    counter = 0

for i in range(N):
    if num_count[i] == 8:
        print(1, end="")
    elif num_count[i] == 9:
        print(4, end="")
    elif num_count[i] == 7:
        print(7, end="")
    elif num_count[i] == 13:
        print(8, end="")
    elif num_count[i] == 12:
        if s[2][4 * i + 2] == ".":
            print(0, end="")
        elif s[1][4 * i + 3] == ".":
            print(6, end="")
        else:
            print(9, end="")
    else:
        if s[3][4 * i + 3] == ".":
            print(2, end="")
        elif s[1][4 * i + 1] == ".":
            print(3, end="")
        else:
            print(5, end="")
print()
